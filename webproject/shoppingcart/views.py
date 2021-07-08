from django.shortcuts import redirect

from webproject.shop.models import Product
from webproject.shoppingcart.shoppingcart import ShoppingCart


def add_product(request, product_id):
    shoppingcart = ShoppingCart(request)
    product = Product(id=product_id)
    shoppingcart.add_product(product)

    return redirect("shop")


def eliminate_product(request, product_id):
    shoppingcart = ShoppingCart(request)
    product = Product(id=product_id)
    shoppingcart.eliminate(product)

    return redirect("shop")


def reduce_product(request, product_id):
    shoppingcart = ShoppingCart(request)
    product = Product(id=product_id)
    shoppingcart.reduce_product(product)

    return redirect("shop")
