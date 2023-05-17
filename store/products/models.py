from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

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

    def __str__(self) -> str:
        return self.name


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.product} - {self.category}"
