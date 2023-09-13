# import os

# from django import setup
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from products.models import Category, Product

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
# setup()


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse("index")
        response = self.client.get(path=path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.template_name, ["products/index.html"])
        # self.assertTemplateUsed(response, "products/index.html")


class ProductsListViewTestCase(TestCase):
    fixtures = ["category.json", "products.json", "productcategory.json"]

    def test_list(self):
        path = reverse("products:index")
        response = self.client.get(path=path)
        self._common_tests(response)

        products = Product.objects.all()
        print(products)
        self.assertEqual(
            list(response.context_data["object_list"]),
            list(products[:3]),
        )

    def test_list_with_category(self):
        category = Category.objects.first()
        path = reverse("products:category", kwargs={"category_id": category.id})
        response = self.client.get(path=path)
        self._common_tests(response)

        filtered_by_category_products = Product.objects.filter(
            categories__in=[category.id]
        )
        self.assertEqual(
            list(response.context_data["object_list"]),
            list(filtered_by_category_products[:3]),
        )

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "products/products.html")
