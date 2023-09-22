import json
import logging
import uuid
from http import HTTPStatus
from typing import Any

from common.views import CommonMixin
from django.conf import settings
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from orders.forms import OrderCreateForm
from orders.models import Order
from products.models import Basket
from yookassa import Configuration, Payment
from yookassa.domain.notification import WebhookNotification

Configuration.account_id = settings.YOOKASSA_SHOP_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY


class SuccessTemplateView(CommonMixin, TemplateView):
    template_name = "orders/success.html"
    title = "Store - Заказ оформлен!"


# Create your views here.
class OrderCreateView(CommonMixin, CreateView):
    template_name = "orders/order_create.html"
    form_class = OrderCreateForm
    success_url = reverse_lazy("orders:order_create")
    success_message = "Заказ успешно оформлен!"
    title = "Store - Оформление заказа"

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        super(OrderCreateView, self).post(request, *args, **kwargs)
        order = self.object
        basket = Basket.objects.filter(user=order.user).last()
        products_basket = basket.productbasket_set.all()

        payment = Payment.create(
            params={
                "amount": {"value": f"{products_basket.total_sum}", "currency": "RUB"},
                "confirmation": {
                    "type": "redirect",
                    "return_url": "{}{}".format(
                        settings.DOMAIN_NAME,
                        reverse("orders:order_success"),
                    ),
                },
                "metadata": {
                    "order_id": order.id,
                },
                "capture": True,
                "description": f"Заказ №{order.id}",
            },
            idempotency_key=uuid.uuid4(),
        )
        return HttpResponseRedirect(
            payment.confirmation.confirmation_url,
            status=HTTPStatus.SEE_OTHER,
        )

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


@csrf_exempt
def payment_yookasssa_webhook_view(request):
    if request.method == "POST":
        try:
            event_json = json.loads(request.body)
            notification = WebhookNotification(event_json)
        except Exception:
            logging.warning(
                "Can't recoginse webhook notification object from event_json in yookassa POST request!"
            )
            return HttpResponse(status=HTTPStatus.NOT_ACCEPTABLE)
        if notification.object.status == "succeeded":
            order_id = notification.object.metadata["order_id"]
            fulfill_order(order_id)
        return HttpResponse(status=HTTPStatus.OK)
    else:
        return HttpResponseRedirect(reverse("index"))


def fulfill_order(order_id: int):
    try:
        order = Order.objects.get(id=order_id)
        if order.status != Order.Status.PAID:
            order.update_after_payment()
    except Order.DoesNotExist:
        logging.warning(
            f"Order with id={order_id} not found in db and can't be fulfilled."
        )
