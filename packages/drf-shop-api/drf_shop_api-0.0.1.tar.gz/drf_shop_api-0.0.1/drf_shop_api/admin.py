from django.contrib import admin

from .models import (
    Currency,
    CurrencyRate,
    CustomerBonusWallet,
    CustomerCart,
    CustomerCartProduct,
    CustomerWishList,
    Order,
    OrderProduct,
    OrderShipping,
    Product,
    ProductCategory,
    ProductComment,
    ProductImage,
    ProductProperty,
    Property,
    ShippingMethod,
    Tax,
)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "title",
        "created_at",
        "updated_at",
        "url",
        "parent",
        "is_active",
    )
    list_filter = ("created_at", "updated_at", "parent", "is_active")
    date_hierarchy = "created_at"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "title",
        "created_at",
        "updated_at",
        "price",
        "currency",
        "category",
        "is_active",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "currency",
        "category",
        "is_active",
    )
    date_hierarchy = "created_at"


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "image", "is_main")
    list_filter = ("product", "is_main")


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "title", "unit")


@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "property", "value")
    list_filter = ("product", "property")


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "content")
    list_filter = ("user", "product")


@admin.register(CustomerBonusWallet)
class CustomerBonusWalletAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "amount")
    list_filter = ("user",)


@admin.register(CustomerWishList)
class CustomerWishListAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "title",
        "created_at",
        "updated_at",
        "user",
    )
    list_filter = ("created_at", "updated_at", "user")
    raw_id_fields = ("products",)
    date_hierarchy = "created_at"


@admin.register(CustomerCart)
class CustomerCartAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at", "user")
    list_filter = ("created_at", "updated_at", "user")
    date_hierarchy = "created_at"


@admin.register(CustomerCartProduct)
class CustomerCartProductAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "product", "quantity")
    list_filter = ("cart", "product")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at", "user", "status")
    list_filter = ("created_at", "updated_at", "user")
    date_hierarchy = "created_at"


@admin.register(OrderShipping)
class OrderShippingAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "method", "address", "status")
    list_filter = ("order", "method")


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity")
    list_filter = ("order", "product")


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "title",
        "dlm",
        "is_active",
        "is_main",
    )
    list_filter = ("dlm", "is_active", "is_main")


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "from_currency",
        "to_currency",
        "rate",
        "is_active",
        "created_at",
    )
    list_filter = ("from_currency", "to_currency", "is_active", "created_at")
    date_hierarchy = "created_at"


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "title",
        "created_at",
        "updated_at",
        "value",
    )
    list_filter = ("created_at", "updated_at")
    date_hierarchy = "created_at"


@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "title", "logo")
