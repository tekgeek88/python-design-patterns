from StateDesignPattern.context import Context
from StateDesignPattern.concrete_state import ConcreteStateA, ConcreteStateB

########################################################
#                   Main Program
########################################################
if __name__ == '__main__':
    context = Context()
    stateA = ConcreteStateA()
    stateB = ConcreteStateB()

    context.setState(stateA)
    context.Handle()

    context.setState(stateB)
    context.Handle()
