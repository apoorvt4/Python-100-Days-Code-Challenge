# class parentclass:
#     def parent_method(self):
#         print("This is the  parent method.1")

# class childclass(parentclass):
#     def parent_method(self):
#         print("Harry")
#         super().parent_method()
#     def child_method(self):
#         print("This is the child method.2")
#         super().parent_method()


# child_object = childclass()
# child_object.child_method()
# child_object.parent_method()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = programmer("Harry", "2345", "python")
print(harry.name)
print(harry.id)
print(harry.lang)
