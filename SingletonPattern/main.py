# from singleton import Singleton
from SingletonPattern.singleton import Singleton
from SingletonPattern.lazy_singleton import LazySingleton

########################################################
#                   Main Program
########################################################

if __name__ == '__main__':

    print("Testing classic singleton")
    s = Singleton()
    print(f"Object created: {s}")
    s2 = Singleton()
    print(f"Object created: {s2}")


    print()
    print("Testing lazy singleton")
    # Initialize class but do not create object
    s1 = LazySingleton()
    # Access the instance and create the object if not created
    print(f"Object created: {LazySingleton.getInstance()}")

    # Try to create another instance and it lets us know it is already created
    s2 = LazySingleton()
