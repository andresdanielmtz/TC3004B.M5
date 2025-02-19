"""
Ejemplo de encaspulación.
"""


def calculateTax(order):
    tax = tax_table[order["country"]]
    if order["country"] == "US":
        tax = us_state[order["state"]]
    return 1 - tax


# Encapsulacion a nivel método.
def getOrder(order):
    tax = calculateTax(order)
    return sum(item["price"] * tax for item in order["items"])


tax_table = {"US": 0.20, "MX": 0.80, "UK": 0.10}
us_state = {"CA": 0.80, "NY": 0.20, "OK": 0}

order = {
    "country": "US",
    "state": "CA",
    "items": [{"name": "Thing", "price": 3000}, {"name": "Thing 2", "price": 1000}],
}

res = getOrder(order=order)
print(f"Total: {res}")
