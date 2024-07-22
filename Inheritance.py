class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetail(self):
        print(f"The name of employee is {self.name} and Id is {self.id}")

class programmer(Employee):
    def showLanguage(self):
        print("The default language is python")

class coder(programmer):
    def showCode(self):
        print("Hi There")
    



e = Employee("Rohan Das", 420)
e.showDetail()
e1 = Employee("Harry Khan", 150)
e1.showDetail()
e2 = ("Apoorv Tiwari", 350)
e2.showDetail()
e3 = Employee("Drishti Jain", 400)
e3.showDetail()
e2.showLanguage()
e2.showCode()
