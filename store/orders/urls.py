from django.contrib.auth.decorators import login_required
from django.urls import path
from orders.views import (
    OrderCreateView,
    OrdersListView,
    SuccessTemplateView,
    payment_yookasssa_webhook_view,
)

app_name = "orders"

urlpatterns = [
    path(
        "order_create/", login_required(OrderCreateView.as_view()), name="order_create"
    ),
    path(
        "order_success/",
        login_required(SuccessTemplateView.as_view()),
        name="order_success",
    ),
    path("webhook_yookassa/", payment_yookasssa_webhook_view, name="webhook_yookassa"),
    path("", login_required(OrdersListView.as_view()), name="orders_list"),
]
