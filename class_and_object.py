class person:
    name = "Apoorv"
    occupation = "Data Scientest"
    networth = 100000
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = person()
b = person()
# a.name = "shubham"
# # a.occupation = "Accountant"
# print(a.name, a.occupation)

b.name = "Nitika"
b.occupation = "HR"

a.info()
b.info()