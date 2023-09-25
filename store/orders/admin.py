from django.contrib import admin

# Register your models here.
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "email",
        "delivery_address",
        "status",
    )
    fields = (
        "id",
        "user",
        "created_at",
        (
            "first_name",
            "last_name",
        ),
        "email",
        "delivery_address",
        "status",
        "basket_history",
    )
    readonly_fields = (
        "id",
        "created_at",
    )
