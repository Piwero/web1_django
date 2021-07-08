from django.conf import settings

class Basket:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}

        self.basket = basket

    def add_product(self, product):
        if str(product.id) not in self.basket.keys():
            self.basket[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "price": str(product.price),
                "quantity": 1,
                "image": product.image.url,
            }
        else:
            for key, value in self.basket.items():
                if key == str(product.id):
                    value["quantity"] += 1
                    break
        self.save_basket()

    def save_basket(self):
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def eliminate(self, product):
        product.id = str(product.id)
        if product.id in self.basket:
            del self.basket[product.id]
            self.save_basket()

    def reduce_product(self, product):
        for key, value in self.basket.items():
            if key == str(product.id):
                value["quantity"] -= 1
                if value["quantity"] < 1:
                    self.eliminate(product)
                break
        self.save_basket()

    def reset_basket(self):
        self.session[settings.BASKET_SESSION_ID] = {}
        self.session.modified = True


