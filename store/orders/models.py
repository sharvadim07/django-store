from django.db import models
from django.utils.translation import gettext_lazy
from products.models import Basket
from users.models import User


# Create your models here.
class Order(models.Model):
    class Status(models.IntegerChoices):
        CREATED = 0, gettext_lazy("Создан")
        PAID = 1, gettext_lazy("Оплачен")
        ON_WAY = 2, gettext_lazy("В пути")
        DELIVERED = 3, gettext_lazy("Доставлен")

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket_history = models.JSONField(default=dict)
    first_name = models.CharField(max_length=62)
    last_name = models.CharField(max_length=62)
    delivery_address = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    status = models.SmallIntegerField(choices=Status.choices, default=Status.CREATED)

    def __str__(self) -> str:
        return f"Order #{self.id} for {self.user.username}"

    def update_after_payment(self):
        self.status = self.Status.PAID
        basket = Basket.objects.filter(user=self.user).last()
        products_basket = basket.productbasket_set.all()
        self.basket_history = {
            "purchsed_items": [
                product_basket.de_json() for product_basket in products_basket
            ],
            "total_sum": float(products_basket.total_sum),
        }
        basket.delete()
        self.save()
