from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.generics import ListAPIView


class ProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
