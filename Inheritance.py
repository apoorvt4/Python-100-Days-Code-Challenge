# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def showDetail(self):
#         print(f"The name of employee is {self.name} and Id is {self.id}")

# class programmer(Employee):
#     def showLanguage(self):
#         print("The default language is python")

# class coder(programmer):
#     def showCode(self):
#         print("Hi There")
    



# e = Employee("Rohan Das", 420)
# e.showDetail()
# e1 = Employee("Harry Khan", 150)
# e1.showDetail()
# e2 = ("Apoorv Tiwari", 350)
# e2.showDetail()
# e3 = Employee("Drishti Jain", 400)
# e3.showDetail()
# e2.showLanguage()
# e2.showCode()


# class Student:
#     def __init__(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id

# class Student_more(Student):
#     def __init__(self, name, age, id, subjects):
#         super().__init__(name, age, id)
#         self.subjects = subjects

#     def Student_Details(self):
#         print(f"The name of student is {self.name}, and the age is {self.age}, and there id is {self.id}, and there subject is {self.subjects}")

# College = Student("Apoorv", 18, "0208CS201019", "Maths")
# # College = Student("Apoorv", 18, "0208CS201019")
# # College = Student("Apoorv", 18, "0208CS201019")
# # College = Student("Apoorv", 18, "0208CS201019")
# College.Student_Details()

# class Student:
#     def __init__(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id

# class Student_more(Student):
#     def __init__(self, name, age, id, subjects):
#         super().__init__(name, age, id)  # Call the parent class constructor
#         self.subjects = subjects
        
#     def Student_Details(self):
#         print(f"The name of student is {self.name}, the age is {self.age}, the ID is {self.id}, and the subject is {self.subjects}")

# College = Student_more("Apoorv", 18, "0208CS201019", "Maths")  # Correct class and number of arguments
# College.Student_Details()