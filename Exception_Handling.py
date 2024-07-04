a = input("Enter the number: ")
print(f"Multiplcation table of {a} is: ")


try:
    for i in range(1, 11):
        print(f"{a} x {i} = {int(a)*i}" )
except Exception as e:
    print("Invalid Input!") 
        
