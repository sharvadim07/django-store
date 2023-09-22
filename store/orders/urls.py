from django.urls import path
from orders.views import (
    OrderCreateView,
    SuccessTemplateView,
    payment_yookasssa_webhook_view,
)

app_name = "orders"

urlpatterns = [
    path("order_create/", OrderCreateView.as_view(), name="order_create"),
    path("order_success/", SuccessTemplateView.as_view(), name="order_success"),
    path("webhook_yookassa/", payment_yookasssa_webhook_view, name="webhook_yookassa"),
]
