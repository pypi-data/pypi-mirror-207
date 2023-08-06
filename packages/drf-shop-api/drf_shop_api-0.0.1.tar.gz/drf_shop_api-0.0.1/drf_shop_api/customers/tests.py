from django.apps import apps
from django.conf import settings
from django.urls import reverse
from mixer.backend.django import mixer

from drf_shop_api.customers.models import CustomerBonusWallet, CustomerCart, CustomerCartProduct, CustomerWishList
from drf_shop_api.customers.serializers import (
    BaseCustomerBonusWalletSerializer,
    BaseCustomerWishListSerializer,
    CustomerCartSerializer,
    CustomerWishListSerializer,
)
from drf_shop_api.products.models import Product
from drf_shop_api.products.serializers import ProductSerializer
from drf_shop_api.tests import BaseAPITest
from drf_shop_api.utils import is_increasing


class TestCustomerBonusWallet(BaseAPITest):
    def setUp(self):
        self.wallet_counts: int = 10
        self.list_url: str = reverse("customers:bonus-wallets-list")
        user_list = mixer.cycle(self.wallet_counts).blend(apps.get_model(f"{settings.AUTH_USER_MODEL}"), is_active=True)
        for i, user in zip(range(self.wallet_counts), user_list):
            mixer.blend(CustomerBonusWallet, user=user, amount=(i + 1) * 10)
        self.target = CustomerBonusWallet.objects.first()

    def test_list_as_admin(self):
        self.create_and_login(email="admin@example.com", is_staff=True, is_superuser=True)
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["count"], self.wallet_counts + 1)

    def test_list_as_owner(self):
        self.authorize(self.target.user)
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(all(key in resp.data for key in list(BaseCustomerBonusWalletSerializer.Meta.fields)))

    def test_list_as_non_auth(self):
        self.logout()
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, 401)

    def test_sort_by_amount(self):
        self.create_and_login(email="admin@example.com", is_staff=True, is_superuser=True)
        resp = self.client.get(f"{self.list_url}?ordering=amount")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(is_increasing([float(item["amount"]) for item in resp.data["results"]]))

    def test_filter_by_user(self):
        self.create_and_login(email="admin@example.com", is_staff=True, is_superuser=True)
        resp = self.client.get(f"{self.list_url}?user={self.target.user.id}")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["user"], self.target.user.id)
        self.assertTrue(all(key in resp.data for key in list(BaseCustomerBonusWalletSerializer.Meta.fields)))


class TestCustomerWishList(BaseAPITest):
    def setUp(self):
        self.wish_list_count: int = 10
        self.list_url: str = reverse("customers:wishlists-list")
        user_list = mixer.cycle(self.wish_list_count).blend(
            apps.get_model(f"{settings.AUTH_USER_MODEL}"),
            is_active=True,
        )
        for i, user in zip(range(self.wish_list_count), user_list):
            products = mixer.cycle(i + 1).blend(Product, price=(i + 1) * 10)
            mixer.blend(CustomerWishList, user=user, products=products)
        self.target = CustomerWishList.objects.first()

    def test_list_as_admin(self):
        self.create_and_login(email="admin@example.com", is_staff=True, is_superuser=True)
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, 200)

    def test_list_as_owner(self):
        self.authorize(self.target.user)
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["user"], self.target.user.id)
        self.assertEqual(len(resp.data["products"]), self.wish_list_count)

    def test_list_as_non_auth(self):
        self.logout()
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, 401)

    def test_filter_by_user(self):
        self.create_and_login(email="admin@example.com", is_staff=True, is_superuser=True)
        resp = self.client.get(f"{self.list_url}?user={self.target.user.id}")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["user"], self.target.user.id)
        self.assertTrue(all(key in resp.data for key in list(BaseCustomerWishListSerializer().Meta.fields)))

    def test_filter_by_product(self):
        self.create_and_login(email="admin@example.com", is_staff=True, is_superuser=True)
        resp = self.client.get(f"{self.list_url}?products={Product.objects.first().id}")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["user"], self.target.user.id)
        self.assertTrue(all(key in resp.data for key in list(BaseCustomerWishListSerializer().Meta.fields)))

    def test_edit_as_owner(self):
        self.authorize(self.target.user)
        product = Product.objects.first()
        data = CustomerWishListSerializer(self.target).data
        data["products"] = [ProductSerializer(product).data]
        resp = self.client.put(f"{self.list_url}{self.target.id}/", data)
        self.target.refresh_from_db()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["user"], self.target.user.id)
        self.assertEqual(len(resp.data["products"]), 1)
        self.assertEqual(resp.data["products"][0]["id"], product.id)


class TestCustomerCart(BaseAPITest):
    def setUp(self):
        self.cart_count: int = 10
        self.list_url: str = reverse("customers:carts-list")
        user_list = mixer.cycle(self.cart_count).blend(
            apps.get_model(f"{settings.AUTH_USER_MODEL}"),
            is_active=True,
        )
        product_list = []
        for i in range(self.cart_count):
            product_list.append(mixer.blend(Product, price=(i + 1) * 10))
        for i, user in zip(range(self.cart_count), user_list):
            _ = mixer.blend(CustomerCart, user=user)
            mixer.blend(CustomerCartProduct, cart=_, product=product_list[i])
        self.target = CustomerCart.objects.first()

    def test_list_as_admin(self):
        self.create_and_login(email="admin@example.com", is_staff=True, is_superuser=True)
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["count"], self.cart_count + 1)

    def test_list_as_owner(self):
        self.authorize(self.target.user)
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["user"], self.target.user.id)

    def test_edit_as_owner_change_quantity(self):
        quantity = 15
        self.authorize(self.target.user)
        data = CustomerCartSerializer(self.target).data
        data["products"][-1]["quantity"] = quantity
        resp = self.client.put(f"{self.list_url}{self.target.id}/", data)
        self.target.refresh_from_db()
        self.assertEqual(self.target.products.last().quantity, quantity)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["user"], self.target.user.id)

    def test_edit_as_owner_change_product(self):
        self.authorize(self.target.user)
        quantity = 15
        product = Product.objects.first()
        data = CustomerCartSerializer(self.target).data
        data["products"][0]["product"] = ProductSerializer(product).data
        data["products"][0]["quantity"] = quantity
        resp = self.client.put(f"{self.list_url}{self.target.id}/", data)
        self.target.refresh_from_db()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["user"], self.target.user.id)
        self.assertEqual(resp.data["products"][0]["id"], product.id)
        self.assertEqual(resp.data["products"][0]["quantity"], quantity)


class CustomUserManager(BaseAPITest):
    def test_customer_manager(self):
        user = self.create(email="admin@example.com")
        self.assertEqual(CustomerBonusWallet.objects.first().user.id, user.id)
        self.assertEqual(CustomerCart.objects.first().user.id, user.id)
        self.assertEqual(CustomerWishList.objects.first().user.id, user.id)
