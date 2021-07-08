def total_basket_quantity(request):

    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["basket"].items():
            total = total + (float(value["price"]) * value["quantity"])
    return {"total_basket_quantity": total}
