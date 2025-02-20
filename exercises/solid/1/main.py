"""
Gestión de Notificaciones
Hecho por Andrés Martínez y David Sánchez
"""

from abc import ABC

class Notification(ABC):
    def __init__(self, type):
        self.type = type

    def printService(self):
        NotificationService.print_type(self.type)


# NotificationService únicamente se encarga de imprimir el contenido.
class NotificationService:
    @staticmethod
    def print_type(string):
        print(f"Se está enviando un archivo a través de {string}.")


def main():
    email = Notification("Correo")
    email.printService()

    sms = Notification("SMS")
    sms.printService()


if __name__ == "__main__":
    main()
