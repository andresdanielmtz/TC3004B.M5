'''
Factory Design Pattern
Andrés Martínez - A00227463

Sodafactory, it creates CocaColaFactory and PepsiFactory
'''

from abc import ABC, abstractmethod


class SodaFactory(ABC):
    def __init__(self):
        self.name = "abstract"
    
    @abstractmethod
    def factory_method(self):
        pass 
    
    
class CocaColaFactory(SodaFactory):
    def __init__(self):
        self.name = "Coca Cola"
    
    
    def factory_method(self):
        print(f"This is the {self.name} Factory. [Powered by Coca Cola]")

class PepsiFactory(SodaFactory):
    def __init__(self):
        self.name = "Pepsi"
    
    def factory_method(self):
        print(f"This is the {self.name} Factory. [Powered by Pepsi] ")
        
pepsi_factory = PepsiFactory()
cocacola_factory = CocaColaFactory()

pepsi_factory.factory_method()
cocacola_factory.factory_method()
