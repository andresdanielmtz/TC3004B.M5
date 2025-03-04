from abc import ABC, abstractmethod

class Laptop(ABC):

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def show_battery(self):
        pass