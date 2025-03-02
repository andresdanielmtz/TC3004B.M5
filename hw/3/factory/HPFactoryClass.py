from factory.ComputerFactoryClass import ComputerFactory

import sys
sys.path.append("..")

from computers.DesktopInterface import Desktop
from computers.HandheldInterface import Handheld
from computers.LaptopInterface import Laptop
from models.HP import HPDesktop, HPLaptop, HPHandheld


class HPFactory(ComputerFactory):
    def create_laptop(self):
        return HPLaptop()

    def create_desktop(self):
        return HPDesktop()

    def create_handheld(self):
        return HPHandheld()
