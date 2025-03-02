from factory.ComputerFactoryClass import ComputerFactory

import sys

sys.path.append("..")

from computers.DesktopInterface import Desktop
from computers.HandheldInterface import Handheld
from computers.LaptopInterface import Laptop
from models.HP import HPDesktop, HPLaptop, HPHandheld
from random import randint


class HPFactory(ComputerFactory):
    def getData(self):
        print(f"Currently operating in over {randint(50, 120)} countries.")

    def create_laptop(self) -> Laptop:
        return HPLaptop()

    def create_desktop(self) -> Desktop:
        return HPDesktop()

    def create_handheld(self) -> Handheld:
        return HPHandheld()
