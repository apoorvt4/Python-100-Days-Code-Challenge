class Employee:
    companyName = "Google"
    number =+1
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.number =+1
    def showDetail(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount} company size {self.number}")

a = Employee("Apoorv")
a.companyName = "Google India"
a.showDetail()
a2 = Employee("Rohan")
a2.raise_amount = 0.05
a2.companyName = "Nestle"
a2.showDetail()

# Employee.showDetail(a)