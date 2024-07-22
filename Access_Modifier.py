class Employee:
    def __init__(self):
        self.__name = "Harry"

a = Employee()
print(a._Employee__name)
print(a.__dir__())