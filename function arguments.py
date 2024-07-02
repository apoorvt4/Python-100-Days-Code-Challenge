# def average(a=5, b=5):
#     print("The average is", (a+b)/2)

# average(1,5)
# def name(fname, mname = "Terminator", lname = "Px5"):
#     name = input("What is your name\n")
#     print("Hello", name, fname, mname, lname)
#     ask = input("What do you want\n")
#     print("Sorry but i can't give you", ask)
#     why = input("but i give you something more special")
#     print(why)
#     print("Here you go this is")


# name("This is")


# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum+i
#     print("Average is", sum / len(numbers))

# average(5,6,7)

def sverage_students(*student):
   
    sum = 0
    for n in student:
        sum = sum+n
       # print("Students average is", sum / len(student))
    return sum / len(student)


c = sverage_students(10, 20, 30)
print(c)


# def name(**name):
#     print("Hello", name['fname'], name['mname'], name['lname'])

# name(fname='apoorv', mname='kumar', lname='tiwari')

# name(fname='apoorva', mname='piku', lname='tiwari')