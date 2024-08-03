class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

e = Employee("Apoorv", 25000)
print(e.name)
print(e.salary)

string = "Apoorv-12000"
e2 = Employee.fromstr(string)
print(e.name)
print(e.salary)

