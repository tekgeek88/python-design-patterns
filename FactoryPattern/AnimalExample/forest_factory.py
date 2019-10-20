from FactoryPattern.AnimalExample.dog import Dog
from FactoryPattern.AnimalExample.cat import Cat

class ForestFactory(object):

    def make_sound(self, object_type):
        return eval(object_type)().do_say()