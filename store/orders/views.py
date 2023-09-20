import uuid
from http import HTTPStatus
from typing import Any

from common.views import CommonMixin
from django.conf import settings
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from orders.forms import OrderCreateForm
from yookassa import Configuration, Payment

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
        payment = Payment.create(
            params={
                "amount": {"value": "5.00", "currency": "RUB"},
                "confirmation": {
                    "type": "redirect",
                    "return_url": "{}{}".format(
                        settings.DOMAIN_NAME,
                        reverse("orders:order_success"),
                    ),
                },
                "capture": True,
                "description": "Заказ №1",
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
