from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm

# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(
                username=username,
                password=password,
            )
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))

    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(
        request=request,
        template_name="users/login.html",
        context=context,
    )


def registration(request):
    return render(
        request=request,
        template_name="users/register.html",
    )