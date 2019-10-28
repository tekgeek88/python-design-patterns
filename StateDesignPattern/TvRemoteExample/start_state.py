from StateDesignPattern.TvRemoteExample.state import State

class StartState(State):
    def doThis(self):
        print("TV Switching ON...")