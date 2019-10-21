from ObserverDesignPattern.subject import Subject

class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(f"{type(self).__name__}: Got {args} from {subject}")


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(f"{type(self).__name__}: Got {args} from {subject}")


########################################################
#                   Main Program
########################################################
if __name__ == '__main__':
    subject = Subject()
    observer1 = Observer1(subject)
    observer2 = Observer2(subject)

    subject.notifyAll('notification')