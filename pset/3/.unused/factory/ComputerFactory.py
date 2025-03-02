from computers.desktop import Desktop
from computers.handheld import Handheld
from computers.laptop import Laptop


class ComputerFactory:
    @staticmethod
    def create_computer(type, order):
        if type == "desktop":
            return Desktop(order)
        elif type == "laptop":
            return Laptop(order)
        elif type == "handheld":
            return Handheld(order)
        else:
            print("Invalid Computer Type, sorry:3")
