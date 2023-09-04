from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


from products.models import Product, Category, Basket, ProductBasket


# Create your views here.
class IndexView(TemplateView):
    template_name = "products/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(IndexView, self).get_context_data()
        context["title"] = "Super store"
        return context


class ProductsListView(ListView):
    model = Product
    template_name = "products/products.html"
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get("category_id")
        queryset = (
            Category.objects.get(id=category_id).product_set.all()
            if category_id
            else queryset
        )
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ProductsListView, self).get_context_data()
        context["title"] = "Store - Каталог"
        context["categories"] = Category.objects.all()
        return context


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
