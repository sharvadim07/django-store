from products.models import Basket, Category, Product, ProductBasket
from rest_framework import fields, serializers
from users.models import User


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


class ProductBasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    # sum = fields.FloatField()

    class Meta:
        model = ProductBasket
        fields = (
            "product",
            "quantity",
            "sum",
        )


class BasketSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        many=False,
        slug_field="username",
        queryset=User.objects.all(),
    )
    products = ProductBasketSerializer(many=True)
    total_sum = fields.SerializerMethodField()
    total_quantity = fields.SerializerMethodField()

    class Meta:
        model = Basket
        fields = (
            "user",
            "created_at",
            "total_sum",
            "total_quantity",
            "products",
        )
        read_only_fields = ("created_at",)

    def get_total_sum(self, obj):
        return ProductBasket.objects.filter(basket_id=obj.user.id).total_sum

    def get_total_quantity(self, obj):
        return ProductBasket.objects.filter(basket_id=obj.user.id).total_quantity
