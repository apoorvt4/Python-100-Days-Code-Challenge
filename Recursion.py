# factorical(n) = n * factorial(n - 1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n - 1)

# 5 * 4 * 3 * 2 * 1 = 120
print(factorial(5))
print(factorial(10))
print(factorial(100))

def factoria1(x):
    if (x==0 or x==5):
        return False
    else:
        return True
    
print(factoria1(-0))

