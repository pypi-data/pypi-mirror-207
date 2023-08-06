import logging
import typing

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from rest_framework import serializers

logger = logging.getLogger("drf_shop")


def is_increasing(lst):
    """
    Check if each next element in a list is greater than the previous element.

    Args:
        lst: A list of numbers.

    Returns:
        True if each next element is greater than the previous element, False otherwise.
    """
    return all(lst[i] > lst[i - 1] for i in range(1, len(lst)))


def qs_admin_or_author(view, qs):
    """qs_admin_or_author
    Returns all models if the user is an admin, otherwise returns
    only the current user's model instance without pagination.

    Args:
        request: HttpRequest object representing the current request.
        model: Django model class representing targeted model.

    """
    # * If admin user return all customer wallet
    if view.request.user.is_staff:
        return qs
    # * Return only current user wallet and remove pagination
    view.list_serializer_class = view.serializer_class
    return qs.filter(user=view.request.user)


def get_deletion_ids(queryset: QuerySet, validated_data: list, lookup_field: str = "id") -> list:
    """Get IDs for queryset that must be deleted from queryset.
    i. e. IDs that are not present in validated_data but present in queryset

    :param queryset: queryset object
    :param validated_data: validated data to find IDs in
    :param lookup_field: what field to use when retrieving deletion ID
    :return: list of IDs for deletion
    """
    model_set = set(queryset.values_list(lookup_field, flat=True))
    values_set = {v[lookup_field] for v in validated_data if lookup_field in v}
    return list(model_set.difference(values_set))


def update_related_objects(self, instance_name, instance, objects_name, objects, serializer):
    """
    Updates related objects of an instance in the database with the given serialized objects.

    Args:
        instance_name (str): The name of the instance being updated.
        instance: The instance being updated.
        objects_name (str): The name of the related objects being updated.
        objects: The updated related objects.
        serializer: The serializer used to serialize the updated related objects
    """
    deletion_ids = get_deletion_ids(getattr(instance, objects_name), objects)
    getattr(instance, objects_name).filter(id__in=deletion_ids).delete()
    save_related({instance_name: instance}, getattr(instance, objects_name), objects, serializer, self.context)


def save_related(
    base: dict,
    queryset: QuerySet,
    validated_data: dict,
    related_serializer_class: typing.Type[serializers.Serializer],
    context: dict = None,
):
    """Save related serializer based on base serializer data

    :param base: base info to pass in related serializer's ``.save(**base)`` method
    :param queryset: queryset to get object from
    :param validated_data: validated data
    :param related_serializer_class: related serializer class
    :param context: parent serializer's context

    :return list of created objects
    """
    response = []
    for v in validated_data:
        id_ = v.pop("id", None)
        if id_:
            try:
                obj = queryset.get(id=id_)
            except ObjectDoesNotExist:
                logger.warning(f"Object  with ID {id_} is not found in db. Skipping.")
                continue
        else:
            obj = None
        related_serializer = related_serializer_class(data=v, instance=obj, context=context)
        related_serializer.is_valid(raise_exception=True)
        obj = related_serializer.save(**base)
        response.append(obj)
    return response


def remove_id_on_create(cls: serializers.ModelSerializer) -> serializers.ModelSerializer:
    """This decorator removes id field from validated_data
    on serializer class create method.

    It highly relies on serializer's context. It uses
    `view` object from the context to ensure that the `create`
    action takes place.

    If the serializer (decorated by this function) is used
    as inline serializer, pass parent serializer's context
    when creating inline serializer's instance.

    :param cls: serializers.ModelSerializer class
    :return: modified class
    """
    old_func = cls.to_internal_value

    def to_internal_value(self, data):
        try:
            is_create = self.context["view"].action == "create"
        except KeyError:
            raise KeyError(
                "The 'remove_id_on_create' decorator relies on serializer's context. The `view` key "
                "should be present in the context as well. If you create the serializer's instance "
                "inside another serializer, ensure that you pass parent serializer's context.",
            )
        if is_create:
            data.pop("id", None)
        return old_func(self, data)

    cls.to_internal_value = to_internal_value
    return cls


def nested_write(validated_data: dict, field_name: str, field_object):
    """Remove nested field value, and replace it with existed element"""
    item = validated_data.setdefault(field_name, None)
    if item:
        validated_data[field_name] = field_object.objects.get(id=item["id"])
    return validated_data
