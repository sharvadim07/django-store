from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "title": "Super store",
        "username": "Vadim",
    }
    # context = {
    #     "title": "Super store",
    #     "username": "Vadim",
    #     "is_promotion": True,
    # }
    return render(
        request,
        "products/index.html",
        context=context
    )


def products(request):
    context = {
        "title": "Store - Каталог",
        "products": [
            {
                "image": "/static/vendor/img/products/Adidas-hoodie.png",
                "name": "Худи черного цвета с монограммами adidas Originals",
                "price": 6090,
                "description": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
            },
            {
                "image": "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
                "name": "Синяя куртка The North Face",
                "price": 23725,
                "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
            },
        ]
    }
    return render(
        request,
        "products/products.html",
        context=context
    )
