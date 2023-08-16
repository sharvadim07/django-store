from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from products.models import Product, Category, Basket, ProductBasket
from users.models import User


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


def products(request, category_id=None):
    if category_id:
        products = Category.objects.get(id=category_id).product_set.all()
    else:
        products = Product.objects.all()
    context = {
        "title": "Store - Каталог",
        "products": products,
        "categories": Category.objects.all(),
    }
    return render(
        request,
        "products/products.html",
        context=context,
    )


@login_required
def add_product_to_basket(request, product_id):
    product = Product.objects.get(id=product_id)
    user_baskets = Basket.objects.filter(user=request.user)
    basket = None
    if user_baskets.exists():
        basket = user_baskets.last()
    else:
        basket = Basket(user=request.user)
        basket.save()
    product_basket = ProductBasket.objects.filter(
        basket=basket,
        product=product,
    ).last()
    if product_basket:
        product_basket.quantity += 1
        product_basket.save()
    else:
        ProductBasket(product=product, basket=basket, quantity=1).save()
    return HttpResponseRedirect(
        request.META["HTTP_REFERER"],
    )


@login_required
def remove_product_from_basket(request, product_basket_id):
    product_basket = ProductBasket.objects.get(id=product_basket_id)
    product_basket.delete()
    return HttpResponseRedirect(
        request.META["HTTP_REFERER"],
    )
