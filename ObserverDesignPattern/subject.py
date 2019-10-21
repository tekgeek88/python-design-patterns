class Subject:

    def __init__(self):
        self.__observers = []

    def observers(self):
        return self.__observers
        # return [type(x).__name__ for x in self.__observers]

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.update(self, *args, **kwargs)

