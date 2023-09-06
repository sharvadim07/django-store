from products.models import Basket, ProductBasket


def products_basket(request):
    user = request.user
    basket = Basket.objects.filter(user=user).last()
    products_basket = ProductBasket.objects.filter(basket=basket)
    return {"products_basket": products_basket if user.is_authenticated else []}
