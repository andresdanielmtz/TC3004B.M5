from abc import ABC, abstractmethod


class SodaFactory(ABC):
    def __init__(self):
        self.name = "abstract"
    
    @abstractmethod
    def factory_method(self):
        pass 