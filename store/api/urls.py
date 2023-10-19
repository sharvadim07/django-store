from api.views import BasketModelViewSet, ProductModelViewSet
from django.urls import include, path
from rest_framework import routers

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductModelViewSet)
router.register(r"baskets", BasketModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
