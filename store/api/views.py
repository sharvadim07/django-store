from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
