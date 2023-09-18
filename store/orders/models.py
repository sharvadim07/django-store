from django.db import models

from users.models import User
from django.utils.translation import gettext_lazy


# Create your models here.
class Order(models.Model):
    class Status(models.IntegerChoices):
        CREATED = 0, gettext_lazy("Created")
        PAID = 1, gettext_lazy("Paid")
        ON_WAY = 2, gettext_lazy("On way")
        DELIVERED = 3, gettext_lazy("Delivered")

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
