from StateDesignPattern.TvRemoteExample.state import State

class TVContext(State):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def doThis(self):
        self.state.doThis()