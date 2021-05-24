class ShoppingCart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        shoppingcart = self.session.get("shoppingcart")
        if not shoppingcart:
            shoppingcart = self.session["shoppingcart"] = {}
        else:
            self.shoppingcart = shoppingcart

    def add_product(self, product):
        if str(product.id) not in self.shoppingcart.keys():
            self.shoppingcart[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "price": str(product.price),
                "quantity": 1,
                "image": product.image.url,
            }
        else:
            for key, value in self.shoppingcart.items():
                if key == str(product.id):
                    value["quantity"] += 1
                    break
        self.save_shopping_cart()

    def save_shopping_cart(self):
        self.session["shoppingcart"] = self.shoppingcart
        self.session.modified = True

    def eliminate(self, product):
        product.id = str(product.id)
        if product.id in self.shoppingcart:
            del self.shoppingcart[product.id]
            self.save_shopping_cart()

    def reduce_product(self, product):
        for key, value in self.shoppingcart.items():
            if key == str(product.id):
                value["quantity"] -= 1
                if value["quantity"] < 1:
                    self.eliminate(product)
                break
        self.save_shopping_cart()

    def reset_shopping_cart(self):
        self.session["shoppingcart"] = {}
        self.session.modified = True
