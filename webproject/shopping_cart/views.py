from django.shortcuts import render
from django.shortcuts import redirect

from webproject.shop.models import Product
from webproject.shopping_cart.shoppingcart import ShoppingCart


def add_product(request, product_id):
    shopping_cart =ShoppingCart(request)
    product = Product(id= product_id)
    shopping_cart.add_product(product)

    return redirect("shop")


def eliminate_product(request, product_id):
    shopping_cart = ShoppingCart(request)
    product = Product(id=product_id)
    shopping_cart.eliminate(product)

    return redirect("shop")


def reduce_product(request, product_id):
    shopping_cart = ShoppingCart(request)
    product = Product(id=product_id)
    shopping_cart.reduce_product(product)

    return redirect("shop")