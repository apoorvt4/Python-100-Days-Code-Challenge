import time

# def usingWhile():
#     i = 0
#     while i<5000:
#       i =  i + 1
#       print(i)

# def usingfor():
#     for i in range(5000):
#        print(i)

# init = time.time()
# usingfor()
# t1 = time.time() - init
# init = time.time()
# usingWhile()
# print(t1)
# print(time.time() - init)

# print(5)
# time.sleep(3)
# print("This is printed after 3 seconds")

t = time.localtime()
formatted_time = time.strftime("%y-%m-%d %H:%M:%S", t)
print(formatted_time)

print(time.gmtime(0))



