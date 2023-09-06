from typing import Any

from common.views import CommonMixin
from django import http
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


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

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super(UserProfileView, self).get_context_data()
    #     basket = Basket.objects.filter(user=self.object).last()
    #     products_basket = ProductBasket.objects.filter(basket=basket)
    #     context["basket"] = basket
    #     context["products_basket"] = products_basket
    #     return context


class EmailVerificationView(CommonMixin, TemplateView):
    title = "Store - Подтверждение email"
    template_name = "users/email_verification.html"

    def get(
        self, request: http.HttpRequest, *args: Any, **kwargs: Any
    ) -> http.HttpResponse:
        code = kwargs["code"]
        email = kwargs["email"]
        user = User.objects.get(email=email)
        email_verifications = EmailVerification.objects.filter(
            user=user,
            code=code,
        )
        if email_verifications.exists() and not email_verifications.last().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("index"))
