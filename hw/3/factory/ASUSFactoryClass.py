from factory.ComputerFactoryClass import ComputerFactory

import sys
sys.path.append("..")
from computers.DesktopInterface import Desktop
from computers.HandheldInterface import Handheld
from computers.LaptopInterface import Laptop
from models.ASUS import ASUSDesktop, ASUSLaptop, ASUSHandheld


class ASUSFactory(ComputerFactory):
    def create_laptop(self) -> Laptop:
        return ASUSLaptop()

    def create_desktop(self) -> Desktop:
        return ASUSDesktop()

    def create_handheld(self) -> Handheld:
        return ASUSHandheld()
