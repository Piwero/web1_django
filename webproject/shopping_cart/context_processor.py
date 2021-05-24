def total_shoppingcart_quantity(request):

    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["shoppingcart"].items():
            total = total + (float(value["price"]) * value["quantity"])
            return {"total_shoppingcart_quantity": total}
