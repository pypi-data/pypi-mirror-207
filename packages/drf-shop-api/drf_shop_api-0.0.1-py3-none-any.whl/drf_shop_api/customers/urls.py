from rest_framework.routers import SimpleRouter

from drf_shop_api.customers.views import CustomerBonusWalletViewSet, CustomerCartViewSet, CustomerWishListViewSet

app_name = "customers"

router = SimpleRouter()
router.register("bonus-wallets", CustomerBonusWalletViewSet, basename="bonus-wallets")
router.register("wishlists", CustomerWishListViewSet, basename="wishlists")
router.register("carts", CustomerCartViewSet, basename="carts")
urlpatterns = [
    *router.urls,
]
