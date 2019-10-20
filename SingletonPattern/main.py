# from singleton import Singleton
from SingletonPattern.singleton import Singleton
from SingletonPattern.lazy_singleton import LazySingleton
from SingletonPattern.meta_singleton import MetaSingleton


def test(description, test):
    print(f"*****  Testing {description}  *****")
    test()
    print(f"*****  Finished testing {description}  *****")
    print()

def test_classic_singleton():
    print("# Creating objects")
    print("s = Singleton()")
    print("s2 = Singleton()")
    s = Singleton()
    s2 = Singleton()
    print(f"Object created: {s}")
    print(f"Object created: {s2}")

def test_lazy_singleton():
    print("# Initialize class but do not create object")
    print("s1 = LazySingleton()")
    s1 = LazySingleton()
    print("# Access the instance and create the object if not created")
    print("LazySingleton.getInstance()")
    print(f"Object created: {LazySingleton.getInstance()}")
    print("# Try to create another instance and it lets us know it is already created")
    s2 = LazySingleton()

def test_meta_singleton():
    print("# Create some loggers using normal instantiation techniques")

    class Logger(metaclass=MetaSingleton):

        def do_logger_stuff(self, message):
            print(f"stuff logged: {message}")

    print("logger1 = Logger()")
    print("logger2 = Logger()")
    logger1 = Logger()
    logger2 = Logger()

    print(f"Logger1: {logger1}")
    print(f"Logger2: {logger2}")

    logger1.do_logger_stuff("Stuff 1")
    logger2.do_logger_stuff("Stuff 2")


def test_meta_singleton_db_example():
    import sqlite3

    class Database(metaclass=MetaSingleton):
        connection = None

        def connect(self):
            if self.connection is None:
                self.connection = sqlite3.connect("database.db")
                self.cursorobj = self.connection.cursor()
            return self.cursorobj

    db1 = Database().connect()
    db2 = Database().connect()

    print(f"Database Object DB1: {db1}")
    print(f"Database Object DB2: {db2}")

########################################################
#                   Main Program
########################################################
if __name__ == '__main__':

    test("classic singleton", test_classic_singleton)

    test("lazy singleton", test_lazy_singleton)

    test("meta singleton", test_meta_singleton)

    test("database example", test_meta_singleton_db_example)
