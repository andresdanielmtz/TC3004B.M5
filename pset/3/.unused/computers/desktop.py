from computers.baseComputer import BaseComputer


class Desktop(BaseComputer):
    def initialize(self):
        super().initialize()
        print("(Desktop)")
        
    def getTemp(self):
        print("This Computer is at 50°C.")

    def boot(self):
        print("This computer took 10 seconds to boot.")
