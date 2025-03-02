import sys
sys.path.append("..")

from computers.DesktopInterface import Desktop
from computers.HandheldInterface import Handheld
from computers.LaptopInterface import Laptop


class HPLaptop(Laptop):
    def boot(self):
        print("Booting up, HP Laptop")
    def show_battery(self):
        print("Showing Battery, HP Laptop")

class HPDesktop(Desktop):
    def boot(self):
        print("Booting up, HP Desktop")


class HPHandheld(Handheld):
    def boot(self):
        print("Booting up, HP Handheld")
    def show_battery(self):
        print("Showing Battery, HP Handheld")