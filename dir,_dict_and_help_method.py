# x = [1, 2, 3]
# print(dir(x))
# print(x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.verson = 1.55

p = Person("Apoorv", 30)
print(p.__dict__)
print(help(Person))