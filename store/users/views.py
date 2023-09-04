from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket, ProductBasket
from users.models import User
from common.views import CommonMixin


# Create your views here.
class UserLoginView(CommonMixin, LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    title = "Store - Авторизация"


class UserRegistrationView(CommonMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = "users/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:login")
    success_message = "Регистрация успешно завершена!"
    title = "Store - Регистрация"


class UserProfileView(CommonMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("users:profile")
    title = "Store - Профиль"

    def get_success_url(self) -> str:
        return reverse_lazy("users:profile", args=(self.object.id,))

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(UserProfileView, self).get_context_data()
        basket = Basket.objects.filter(user=self.object).last()
        products_basket = ProductBasket.objects.filter(basket=basket)
        context["basket"] = basket
        context["products_basket"] = products_basket
        return context
