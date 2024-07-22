# def greet(fx):
#     def mfx(*args, **kwargs):
#        print("Good Morning")
#        fx(*args, **kwargs)
#        print("Thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("Hello World")
# @greet
# def add(a, b):
#     print(a+b)

# hello()
# add(5, 4)

def last_message(exit):
    def good_by():
        print("Good Morning", exit, "!")
        good_by()
        print("Good By Buddy")
    return good_by

@last_message
def name():
    return "Apoorv"

name()


