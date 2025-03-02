from computers.baseComputer import BaseComputer


class Laptop(BaseComputer):

    def initialize(self):
        super().initialize()
        print("(Laptop)")

    def getTemp(self):
        print("This laptop is at 110°C")

    def boot(self):
        print("This computer took 2 seconds to boot.")
