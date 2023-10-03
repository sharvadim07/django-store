from api.views import ProductsListAPIView
from django.urls import path

app_name = "api"

urlpatterns = [
    path("product_list/", ProductsListAPIView.as_view(), name="product_list")
]
