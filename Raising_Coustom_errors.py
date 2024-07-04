a = int(input("Enter any value between 5 and 9: "))

if(str(a)=='quit'):
    print("Quit")
elif(int(a)<5 or int(a)>9):
    raise ValueError("Enter any value between 5 and 9")





