from django.urls import path

from products.views import (
    products,
    add_product_to_basket,
    remove_product_from_basket,
)

app_name = "products"

urlpatterns = [
    path("", products, name="index"),
    path("category/<int:category_id>", products, name="category"),
    path(
        "basket/add/<int:product_id>/",
        add_product_to_basket,
        name="add_product_to_basket",
    ),
    path(
        "basket/remove/<int:product_basket_id>/",
        remove_product_from_basket,
        name="remove_product_from_basket",
    ),
]
