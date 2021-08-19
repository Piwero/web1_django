from django.shortcuts import redirect

from shop.models import Product

from .basket import Basket


def add_product(request, product_id):
    basket = Basket(request)
    product = Product.objects.get(id=product_id)
    basket.add_product(product)

    return redirect("shop")


def eliminate_product(request, product_id):
    basket = Basket(request)
    product = Product.objects.get(id=product_id)
    basket.eliminate(product)

    return redirect("shop")


def reduce_product(request, product_id):
    basket = Basket(request)
    product = Product.objects.get(id=product_id)
    basket.reduce_product(product)

    return redirect("shop")


def reset_basket(request):
    basket = Basket(request)
    basket.reset_basket()

    return redirect("shop")
