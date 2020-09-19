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

num1 = 10 # Global
def num(n):
 #   num1 = 5  # taking its value from local variable
    print(num1)  # after commenting local variable it takes its value from the global variable
    print("hello")

num("hello world!")
print(num1)   # takes its value from the global variable

