"""
Patron Adapter
Configuracion de Objectos con interfaces incompatibles en primera instancia.

Información tomada desde
https://refactoring.guru/design-patterns/adapter
"""

from abc import ABC, abstractmethod

# Paypal, Strip y Mercadopago,
# Cada una tendrá una implementación distinta :3


# Clase de servicio de pago externo
class PaypalService:
    def send_payment(self, amount: float):
        print(f"Paypal: {amount} payment has been sent")


class StripeService:
    def send_request(self, amount: float):
        print(f"Stripe: {amount} payment has been sent")


class MercadoPagoService:
    def send_money(self, amount: float):
        print(f"MercadoPago: {amount} payment has been sent")

# 1. Interfaz de pago 
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass
    
# 2. Clases adaptadores 
class PaypalAdapter(PaymentProcessor):
    def __init__(self, paypal_service: PaypalService):
        self.paypal_service = paypal_service

    def process_payment(self, amount: float):
        self.paypal_service.send_payment(amount)
    
def main():
    payment_amount = 100
    paypal_processor = PaypalAdapter(PaypalService())
    
    print("Usando paypal")
    paypal_processor.process_payment(payment_amount)
    
if __name__ == "__main__":
    main()