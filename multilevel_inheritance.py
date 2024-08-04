# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"species: {self.species}")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def show_details(self):
#         Animal.show_details(self)
#         print(f"breed{self.breed}")

# class GoldenReteriver(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retriever")
#         self.color = color

#     def show_details(self):
#         Dog.show_details(self)
#         print(f"color: {self.color}")

# o = GoldenReteriver("Tommy", "Black")
# o.show_details()


class Base:
    def __init__(self, name, roll, role):
        self.name = name
        self.roll = roll
        self.role = role


class Intermidate(Base):
    def __init__(self, name, roll, role, age):
        super().__init__(name, roll, role)
        self.age = age

class Derived(Intermidate):
    def __init__(self, name, roll, role, age):
        super().__init__(name, roll, role, age)

    def print_Data(self):
        print(f"The Name is: {self.name}")
        print(f"The Age is: {self.age}")
        print(f"The Roll is: {self.roll}")
        print(f"The Role is: {self.role}")

obj = Derived("Apoorv Tiwari", 2555, "Software Developer", 21)
obj.print_Data()