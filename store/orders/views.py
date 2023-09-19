from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from orders.forms import OrderCreateForm


# Create your views here.
class OrderCreateView(CreateView):
    template_name = "orders/order_create.html"
    form_class = OrderCreateForm
    success_url = reverse_lazy("orders:order_create")
