from StateDesignPattern.state import State


class ConcreteStateA(State):
    def Handle(self):
        print("ConcreteStateA")


class ConcreteStateB(State):
    def Handle(self):
        print("ConcreteStateB")



