from abc import ABC, abstractmethod


class Handheld(ABC):

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def show_battery(self):
        pass
