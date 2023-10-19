from api.my_permissions import IsStaffOrReadOnly
from products.models import Basket, Product
from products.serializers import BasketSerializer, ProductSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsStaffOrReadOnly,)


class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            product_id = request.data["product_id"]
        except KeyError:
            return Response(
                {"product_id": "Field is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            basket, is_created = Basket.create_or_update(product_id, request.user)
        except Product.DoesNotExist:
            return Response(
                {"product_id": f"product_id {product_id} DoesNotExist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        status_code = status.HTTP_201_CREATED if is_created else status.HTTP_200_OK
        serializer = self.get_serializer(basket)
        return Response(serializer.data, status=status_code)
