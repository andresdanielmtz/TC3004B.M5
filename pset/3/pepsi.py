from factory import SodaFactory

class PepsiFactory(SodaFactory):
    def __init__(self):
        self.name = "Pepsi"
    
    def factory_method(self):
        print(f"This is the {self.name} Factory. [Powered by Pepsi] ")
