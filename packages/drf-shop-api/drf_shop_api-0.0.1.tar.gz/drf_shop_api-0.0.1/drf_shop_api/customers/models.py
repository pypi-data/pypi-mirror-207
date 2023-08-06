from django.core.validators import MinValueValidator
from django.db import models

from drf_shop_api.abstract_models import (
    OwnershipMultipleModel,
    OwnershipSingleModel,
    TimeStampedModel,
    TitleDescriptionModel,
)
from drf_shop_api.products.models import Product


class CustomerBonusWallet(OwnershipSingleModel):
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    class Meta:
        db_table = "customer-bonus-wallet"
        ordering = ("-id",)


class CustomerWishList(OwnershipMultipleModel, TimeStampedModel, TitleDescriptionModel):
    products = models.ManyToManyField(Product, blank=True)

    class Meta:
        db_table = "customer-wish-list"
        ordering = ("-id",)


class CustomerCart(OwnershipSingleModel, TimeStampedModel):
    class Meta:
        db_table = "customer-cart"
        ordering = ("-id",)


class CustomerCartProduct(models.Model):
    cart = models.ForeignKey(CustomerCart, models.CASCADE, related_name="products")
    product = models.ForeignKey(Product, models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = "customer-cart-product"
        unique_together = ["cart", "product"]
        ordering = ("-id",)
