# Decorators
# A decorator takes in a function, adds some functionality and returns it.
# Python has an interesting feature called decorators to add functionality to an existing code.
#
# This is also called metaprogramming because a part of the program tries to modify another part of the program
# at compile time.

def function_1():
    print("hello world")

func = function_1
del function_1

print(func())


# we can put function into an function as an argument
#
def result(func):
    func("helo")

result(print)

def decoretor_1(func1):