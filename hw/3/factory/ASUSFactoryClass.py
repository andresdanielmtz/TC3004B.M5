from factory.ComputerFactoryClass import ComputerFactory

import sys
sys.path.append("..")
from computers.DesktopInterface import Desktop
from computers.HandheldInterface import Handheld
from computers.LaptopInterface import Laptop
from models.ASUSProducts import ASUSDesktop, ASUSLaptop, ASUSHandheld


class ASUSFactory(ComputerFactory):
    def advertisement(self):
        print("""\n\n\n
              ---
              ASUS: Where the magic happens!
              ---
              \n\n\n""")
    
    def create_laptop(self) -> Laptop:
        return ASUSLaptop()

    def create_desktop(self) -> Desktop:
        return ASUSDesktop()

    def create_handheld(self) -> Handheld:
        return ASUSHandheld()
