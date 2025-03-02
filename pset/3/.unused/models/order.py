from models import computerPrices


class Order:
    def __init__(self, name, computerType, quantity) -> None:
        self.name = name
        self.computerType = computerType
        self.quantity = quantity

    def calculate_order_cost(self):
        if self.computerType not in computerPrices:
            print("Error while fetching price: Price is unavailable.")
            return
        return computerPrices[self.computerType] * self.quantity
    