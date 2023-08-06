from django.db import transaction
from rest_framework import serializers

from drf_shop_api.customers.models import CustomerBonusWallet, CustomerCart, CustomerCartProduct, CustomerWishList
from drf_shop_api.products.models import Product
from drf_shop_api.products.serializers import ProductSerializer
from drf_shop_api.utils import update_related_objects


class BaseCustomerBonusWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBonusWallet
        fields = ("id", "user", "amount")


# TODO: Add expanded serializer based on user profile serializer from parent project
class BaseCustomerWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerWishList
        fields = ("id", "user", "products")


class CustomerWishListSerializer(BaseCustomerWishListSerializer):
    id = serializers.IntegerField(required=False)
    products = ProductSerializer(many=True)

    @transaction.atomic
    def update(self, instance: CustomerWishList, validated_data: dict) -> CustomerWishList:
        products = validated_data.pop("products", [])
        wish_list = super().update(instance, validated_data)
        product_list = [Product.objects.get(id=product["id"]) for product in products]
        wish_list.products.set(product_list)
        return super().update(instance, validated_data)


class CustomerCartProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CustomerCartProduct
        fields = ("id", "product", "quantity")


class BaseCustomerCartSerializer(serializers.ModelSerializer):
    products = CustomerCartProductSerializer(many=True)

    class Meta:
        model = CustomerCart
        fields = ("id", "user", "products")


class CustomerCartSerializer(BaseCustomerCartSerializer):
    products = CustomerCartProductSerializer(many=True)

    @transaction.atomic
    def update(self, instance: CustomerCart, validated_data: dict) -> CustomerCart:
        products = validated_data.pop("products", None)
        cart = super().update(instance, validated_data)
        if products is not None:
            update_related_objects(self, "cart", cart, "products", products, CustomerCartProductSerializer)
        return cart
