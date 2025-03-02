import sys
sys.path.append("..")

from computers.LaptopInterface import Laptop
from computers.DesktopInterface import Desktop
from computers.HandheldInterface import Handheld


class ASUSLaptop(Laptop):
    def boot(self):
        print("Booting up, ASUS Laptop")
    def show_battery(self):
        print("Showing Battery, ASUS Laptop")

class ASUSDesktop(Desktop):
    def boot(self):
        print("Booting up, ASUS Desktop")


class ASUSHandheld(Handheld):
    def boot(self):
        print("Booting up, ASUS Handheld")
    def show_battery(self):
        print("Showing Battery, ASUS Handheld")