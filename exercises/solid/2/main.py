"""
Sistema de Pagos
Hecho por Andrés Martínez y David Sánchez
"""

from abc import ABC  # abstract base class


class Payment(ABC):
    def __init__(self, payment_types):
        self.payment_types = payment_types

    def pay(self, payment_type):
        if payment_type not in self.payment_types:
            print(
                "Transacción Invalida: El tipo de pago no es aceptado por la institución actualmente. Vuelva pronto. "
            )
            return

        # Únicamente es HSBC pero se puede expandir a otros bancos en el futuro.
        if payment_type == "HSBC":
            PaymentSystem.hsbc()
        elif payment_type == "Paypal":
            PaymentSystem.paypal()
        else:
            PaymentSystem.default()


class PaymentSystem:
    @staticmethod
    def hsbc():
        print("Transaccion por HSBC")

    @staticmethod
    def paypal():
        print("Transaccion por PayPal")

    @staticmethod
    def default():
        print("Transacción realizada en sistema genérico.")


def main():
    shopify = Payment(["Paypal", "BBVA"])
    shopify.pay("Paypal")  # Transaccion por PayPal
    shopify.pay("BBVA")  # Transacción realizada en sistema genérico.
    shopify.pay(
        "Banco de Mexico"
    )  # Transacción Invalida: El tipo de pago no es aceptado por la institución actualmente. Vuelva pronto.


if __name__ == "__main__":
    main()
