from django import forms
from django.utils.translation import gettext_lazy
from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": gettext_lazy("First name"),
            }
        ),
        required=True,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": gettext_lazy("Last name"),
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "you@example.com",
            }
        ),
        required=True,
    )
    delivery_address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": gettext_lazy("Address"),
            }
        ),
        required=True,
    )

    class Meta:
        model = Order
        fields = (
            "first_name",
            "last_name",
            "email",
            "delivery_address",
        )
