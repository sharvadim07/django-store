from django.contrib import admin
from products.models import Basket, Category, Product, ProductBasket

# Register your models here.

admin.site.register(Category)


class ProductCategoryInline(admin.TabularInline):
    model = Product.categories.through
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "quantity",
        "price",
    )
    fields = (
        "name",
        "short_description",
        "description",
        (
            "quantity",
            "price",
        ),
        "image",
    )
    # readonly_fields = ()
    search_fields = (
        "name",
        "description",
        "short_description",
    )
    ordering = (
        "name",
        "-quantity",
    )
    inlines = (ProductCategoryInline,)

    def category(self, object):
        return [category.name for category in object.categories.all()]


class ProductBasketInline(admin.TabularInline):
    model = ProductBasket
    readonly_fields = ("sum",)
    extra = 0


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "products",
        "created_at",
    )
    inlines = (ProductBasketInline,)

    def products(self, object):
        products_basket = ProductBasket.objects.filter(
            basket=object,
        )
        return [product_basket.product.name for product_basket in products_basket]
