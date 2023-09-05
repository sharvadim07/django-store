import uuid
from datetime import timedelta
from django.utils import timezone

from typing import Any
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)
from django import forms
from users.models import User, EmailVerification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите имя пользователя",
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите пароль",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите имя",
            }
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите фамилию",
            }
        ),
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите имя пользователя",
            }
        ),
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите адрес эл. почты",
            }
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите пароль",
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Подтвердите пароль",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def save(self, commit: bool = True) -> Any:
        user = super(UserRegistrationForm, self).save(commit)
        code = uuid.uuid4()
        expiration = timezone.now() + timedelta(days=2)
        record = EmailVerification.objects.create(
            user=user,
            code=code,
            expiration=expiration,
        )
        record.send_verification_email()
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
            }
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
            }
        ),
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "readonly": True,
            }
        ),
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control py-4",
                "readonly": True,
            }
        ),
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "custom-file-input"}),
        required=False,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "image",
        )
