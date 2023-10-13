from products.models import Category, Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True,
        slug_field="name",
        queryset=Category.objects.all(),
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
