from computers.baseComputer import BaseComputer

class Handheld(BaseComputer):
    def initialize(self):
        super().initialize()
        print("(Handheld)")
        
    def getTemp(self):
        print("This computer is at 70°C.")
    def boot(self):
        print("This handheld took 30 seconds to boot.")