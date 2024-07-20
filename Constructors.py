class person:
    def __init__(self, n, o):
        print("Hey i am a person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("Apoorv", "Developer")
b = person("Divya", "HR")
# c = person(1, 2)
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
a.info()
b.info()
# c.info()