'''
Archivo principal, PSET #1
'''

from Order import Order

order = Order(
    "Orden #1",
    [
        {"name": "Jugo", "price": 100, "amount": 1},
        {"name": ":D", "price": 10, "amount": 1},
    ],
    "US",
    "CA",
    "PK",
)
total = order.get_tax_order()

print(f"El total que se va a pagar es {total}")
