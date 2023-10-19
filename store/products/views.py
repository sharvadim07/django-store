from typing import Any, Dict

from common.views import CommonMixin
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.db.models.query import QuerySet
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from products.models import Basket, Category, Product, ProductBasket


# Create your views here.
class IndexView(CommonMixin, TemplateView):
    template_name = "products/index.html"
    title = "Super store"


class ProductsListView(CommonMixin, ListView):
    model = Product
    template_name = "products/products.html"
    paginate_by = 3
    title = "Store - Каталог"
    ordering = "id"

    def get_queryset(self) -> QuerySet[Any]:
        cached_products = cache.get("products")
        if cached_products:
            queryset = cached_products
        else:
            queryset = super(ProductsListView, self).get_queryset()
            cache.set("products", queryset, 30)
        category_id = self.kwargs.get("category_id")
        queryset = (
            # Category.objects.get(id=category_id).product_set.all()
            queryset.filter(categories__in=[category_id])
            if category_id
            else queryset
        )
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ProductsListView, self).get_context_data()
        cached_categories = cache.get("categories")
        if cached_categories:
            context["categories"] = cached_categories
        else:
            context["categories"] = Category.objects.all()
            cache.set("categories", context["categories"], 30)
        return context


@login_required
def add_product_to_basket(request, product_id):
    Basket.create_or_update(product_id, request.user)
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
