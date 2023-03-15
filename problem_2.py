class Product:
    def __init__(self, name, cost, vat_percentage):
        self.name = name
        self.cost = cost
        self.vat_percentage = vat_percentage


class Client:
    def __init__(self, name, citizenship, discount_card_percentage):
        self.name = name
        self.citizenship = citizenship
        self.discount_card_percentage = discount_card_percentage


class YourCart:
    def __init__(self, client):
        self.client = client

    def get_total_price(self, products):
        total_cost = 0
        for product in products:
            cost = product.cost
            if self.client.citizenship != "Belarus":
                cost -= cost * product.vat_percentage / 100
            cost -= cost * self.client.discount_card_percentage / 100
            total_cost += cost
        return total_cost
