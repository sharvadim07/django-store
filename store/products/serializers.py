from products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True,
        slug_field="name",
        read_only=True,
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "image",
            "description",
            "short_description",
            "price",
            "quantity",
            "categories",
        )
