y = 4
print(y)

def hello():
    global  y
    y = 10
    x = 5
    print(x)
    print("Hello apoorv")

hello()
print(f"The global x is {y}")