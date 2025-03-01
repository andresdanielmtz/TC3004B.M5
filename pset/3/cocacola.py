from factory import SodaFactory

class CocaColaFactory(SodaFactory):
    def __init__(self):
        self.name = "Coca Cola"
    
    
    def factory_method(self):
        print(f"This is the {self.name} Factory. [Powered by Coca Cola]")