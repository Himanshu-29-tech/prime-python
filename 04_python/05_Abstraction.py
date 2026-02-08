#============ Abstraction =============
#Hiding internal details & showing only essential features
#Absrtract class --0>> blureprint of other class

from abc import ABC, abstractmethod #(abstraction based classes)
#Abstract class ->> that's willl not be performed
class Animal(ABC):
    def make_sound():
        pass


        
class Lion(Animal):
    def make_sound(self):
        print("Roar!")
class Cow(Animal):
    def make_sound(self):
        print("Moo!")

lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()

 