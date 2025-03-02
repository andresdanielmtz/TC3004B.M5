from abc import ABC, abstractmethod


class ComputerFactory(ABC):
    @abstractmethod
    def create_laptop(self):
        return
    
    @abstractmethod
    def create_handheld(self):
        pass 
    
    @abstractmethod
    def create_desktop(self):
        pass