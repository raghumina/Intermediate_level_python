# A variable is only available from inside the region it is created. This is called scope.
# Local Scope: A variable created inside a function belongs to the local scope of that function,
# and can only be used inside that function

# global scope: A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#
# Global variables are available from within any scope, global and local.

# In easy words global variable is a main variable or we can say a variable that i functions or blocks of code can use in
# a program ant its value will remain consistant
# whereas a local variable will only present inside a fiunction or block of code and works only in it its presence is local

# for example
'''
num1 = 10  # Global


def num(n):
    #   num1 = 5  # taking its value from local variable
    print(num1)  # after commenting local variable it takes its value from the global variable
    print("hello")


num("hello world!")
print(num1)  # takes its value from the global variable
'''
# inside a function a varible first search value form local variable. if local variable is not present in a function then
# it searches from global variable if global variable dont have that related variable value then it throws error
# we can use a global variable inside a function or outside of it but we cant use a local variable outside its block or function

# GLOBAL KEYWORD IF WE WANT TO CHANGE THE VALUE OF A LOCAL VARIABLE IN A SPECIFIC FUNCTION OR CHUNK OF CODE THEN WE
# USES GLOBAL KEYWORD WITHOUT IT WE CANT CHANGE A GLOBAL VARIABLE FOR A SPECIFIC FUNCTION

# FOR EXAMPLE
n = 5


def change():
    global n   # global keyword gives permission to change its value in specific function
    n = n + 23  #

    print(n, "hurray we changed the value with help of global keyword")


print(change())


