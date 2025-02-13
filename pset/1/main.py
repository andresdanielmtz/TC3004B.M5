from order import Order

personal_order = {
    "id": 1252,
    "items": [
        {"name": "thing 1", "price": 500, "amount": 500},
        {"name": "thing 1", "price": 500, "amount": 500},
    ],
}

res = Order(personal_order)
res.printTotal()