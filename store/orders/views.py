from django.views.generic.edit import CreateView
from orders.forms import OrderForm


# Create your views here.
class OrderCreateView(CreateView):
    template_name = "orders/order_create.html"
    form_class = OrderForm
