from django.db import models
from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to="products_images")
    description = models.TextField()
    short_description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
    )
    quantity = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.name


# class ProductCategory(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.PROTECT)

#     def __str__(self) -> str:
#         return f"Продукт: {self.product} - Категория: {self.category}"


class Basket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Корзина для {self.user.username}"


class ProductBasketQuerySet(models.QuerySet):
    @property
    def total_sum(self):
        return sum(product_basket.sum for product_basket in self)

    @property
    def total_quantity(self):
        return sum(product_basket.quantity for product_basket in self)


class ProductBasket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    objects = ProductBasketQuerySet.as_manager()

    @property
    def sum(self):
        return self.product.price * self.quantity
