# # factorical(n) = n * factorial(n - 1)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n - 1)

# # 5 * 4 * 3 * 2 * 1 = 120
# print(factorial(5))
# print(factorial(10))
# print(factorial(100))

# def factoria1(x):
#     if (x==0 or x==5):
#         return False
#     else:
#         return True
    
# print(factoria1(5))

#  This method is for fibonacci series
def fibonacci(f):
    if (f==0):
        return 0
    elif (f==1):
        return 1
    else:
        return (f - 1) + (f - 2)
    
print(fibonacci(0))
