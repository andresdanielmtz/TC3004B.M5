from abc import ABC, abstractmethod


class BaseComputer(ABC):
    def __init__(self, order):
        self.order = order

    @abstractmethod
    def initialize(self):
        print(f"Initialized with the name of {self.order.name}")

    @abstractmethod
    def getTemp(self):
        pass

    @abstractmethod
    def boot(self):
        pass
