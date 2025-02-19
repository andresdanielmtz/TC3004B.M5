"""
Clase Order. PSET #1
"""


class Order:
    def __init__(self, name, items, country, state, city):
        self.__name = name
        self.__items = items
        self.__country = country
        self.__state = state
        self.__city = city
        self.__tax_calculator = TaxCalculator()

        print(f"The country is {self.__country}")

    def get_items(self):
        return self.__items

    def get_name(self):
        return self.__name

    def get_country(self):
        return self.__country

    def get_state(self):
        return self.__state

    def get_city(self):
        return self.__city

    def get_tax_order(self):
        total = sum(item["price"] * item["amount"] for item in self.get_items())
        return total + (
            total
            * self.__tax_calculator.get_tax_order(
                self.get_country(), self.get_state(), self.get_city()
            )
        )


class TaxCalculator:
    def get_tax_order(self, country, state, city):
        tax = 0
        if country == "US":
            tax = self.get_us_tax(state, city)
        elif country == "UK":
            tax = self.get_uk_tax()

        print(f"The tax is {tax}")
        return tax

    def get_us_tax(self, state, city):
        if state == "CA":
            return 0.9
        if city == "NY":
            return 0.99
        return 0.12  # US tax

    def get_uk_tax(self):
        return 1
