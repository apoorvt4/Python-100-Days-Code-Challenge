class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


    def make_sound(self):
        print("sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("Bark!")


class Cat(Animal):
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def make_sound(self):
        print("Meow Meow!")

    def Eat(self):
        print("mouse")

d = Dog("Dog", "Jerman sefard")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

c = Cat("Cat", "black")
c.make_sound()
c.Eat()