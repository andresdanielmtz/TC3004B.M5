from abc import ABC, abstractmethod


class Desktop(ABC):

    @abstractmethod
    def boot(self):
        pass
