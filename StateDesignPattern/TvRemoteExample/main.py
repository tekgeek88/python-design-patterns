from StateDesignPattern.TvRemoteExample.context import TVContext
from StateDesignPattern.TvRemoteExample.start_state import StartState
from StateDesignPattern.TvRemoteExample.stop_state import StopState

########################################################
#                   Main Program
########################################################
if __name__ == '__main__':
    context = TVContext()

    print(f"Initial state: {context.getState()}")

    start = StartState()
    stop = StopState()

    context.setState(stop)
    context.doThis()

    context.setState(start)
    context.doThis()