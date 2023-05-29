from django.shortcuts import render


# Create your views here.
def login(request):
    return render(
        request=request,
        template_name="users/login.html",
    )


def registration(request):
    return render(
        request=request,
        template_name="users/register.html",
    )