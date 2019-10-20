from FactoryPattern.AnimalExample.forest_factory import ForestFactory

########################################################
#                   Main Program
########################################################
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound? Dog or Cat?")
    ff.make_sound(animal)