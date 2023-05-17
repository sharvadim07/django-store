from django.shortcuts import render

from products.models import Product, Category


# Create your views here.
def index(request):
    context = {
        "title": "Super store",
        "username": "Vadim",
    }
    return render(
        request,
        "products/index.html",
        context=context,
    )


def products(request):
    context = {
        "title": "Store - Каталог",
        "products": Product.objects.all(),
        "categories": Category.objects.all(),
    }
    return render(
        request,
        "products/products.html",
        context=context,
    )
