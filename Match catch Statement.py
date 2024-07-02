# x = int(input("Enter the value of x\n"))

# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("case is 4")

#     case _ if x != 90:
#         print(x, "is not 90")
#     case _ if x != 80:
#         print(x, "is not 80")
#     case _:
#         print(x)


print("Enter The Vote From the list 1, 2, 3")
vote = int(input("Enter Your Vote\n"))

match vote:
    case 1:
        print("You Vote To AAM ADMI PARTY")
    case 2:
        print("You Vote To BHARTIYA JANTA PARTY")
    case 3:
        print("You Vote To CONGRESS PART")
    case _:
        print("Enter The Correct Vote!")
