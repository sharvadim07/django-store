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
    image = models.ImageField(upload_to="products_images", blank=True)
    description = models.TextField()
    short_description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=False,
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
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Корзина для {self.user.username}"

    @classmethod
    def create_or_update(cls, product_id, user):
        product = Product.objects.filter(id=product_id).last()
        if not product:
            raise Product.DoesNotExist()
        is_created = False
        basket = Basket.objects.filter(user=user).last()
        if not basket:
            basket = Basket(user=user)
            basket.save()
            is_created = True
        product_basket = ProductBasket.objects.filter(
            basket=basket,
            product=product,
        ).last()
        if product_basket:
            product_basket.quantity += 1
            product_basket.save()
        else:
            product_basket = ProductBasket(
                product=product, basket=basket, quantity=1
            ).save()
        return basket, is_created


class ProductBasketQuerySet(models.QuerySet):
    @property
    def total_sum(self):
        return sum(product_basket.sum for product_basket in self)

    @property
    def total_quantity(self):
        return sum(product_basket.quantity for product_basket in self)


class ProductBasket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket = models.ForeignKey(
        Basket, related_name="products", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=0)

    objects = ProductBasketQuerySet.as_manager()

    @property
    def sum(self):
        return self.product.price * self.quantity

    def de_json(self):
        basket_item = {
            "product_name": self.product.name,
            "quantity": self.quantity,
            "price": float(self.product.price),
            "sum": float(self.sum),
        }
        return basket_item
