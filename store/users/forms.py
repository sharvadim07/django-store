from django.contrib.auth.forms import AuthenticationForm
from django import forms
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "id": "inputEmailAddress",
                "type": "text",
                "placeholder": "Введите имя пользователя",
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control py-4",
                "id": "inputPassword",
                "type": "password",
                "placeholder": "Введите пароль",
            }
        ),
    )
    class Meta:
        model = User
        fields = ("username", "password")
