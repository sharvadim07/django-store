from products.models import Basket, ProductBasket


def products_basket(request):
    user = request.user
    if user.is_authenticated:
        basket = Basket.objects.filter(user=user).last()
        if basket:
            return {"products_basket": ProductBasket.objects.filter(basket=basket)}
        else:
            return {"products_basket": []}
    else:
        return {"products_basket": []}
