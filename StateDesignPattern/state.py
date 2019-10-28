from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):

    @abstractmethod
    def Handle(self):
        pass


