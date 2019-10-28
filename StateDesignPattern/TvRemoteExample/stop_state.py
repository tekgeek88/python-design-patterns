from StateDesignPattern.TvRemoteExample.state import State

class StopState(State):
    def doThis(self):
        print("TV Switching OFF...")