from django.urls import path
from products.views import (
    ProductsListView,
    add_product_to_basket,
    remove_product_from_basket,
)

# from django.views.decorators.cache import cache_page

app_name = "products"

urlpatterns = [
    # Caching entire page
    # path("", cache_page(timeout=30)(ProductsListView.as_view()), name="index"),
    path("", ProductsListView.as_view(), name="index"),
    path("page/<int:page>", ProductsListView.as_view(), name="paginator"),
    path("category/<int:category_id>", ProductsListView.as_view(), name="category"),
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
