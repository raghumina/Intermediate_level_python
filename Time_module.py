# Time module in python
# Module which provides functions for working with times, and for converting between representations.
# The function time. time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch).

import time

curremt_time = time.time()

print(curremt_time)

# we can use this module to find hte time, the time taken in execution of the program
# or in many other ways

# lets compare time of two programs
import numpy as np
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))

none
edit
play_arrow

brightness_4


# Python program to
# demonstrate instantiating
# a class


class Dog:
    # A simple class
    # attribute
    attr1 = "mamal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

    # Driver code


edit
play_arrow

brightness_4


def test_method(self):
    print("This is Test class method!")


# creating a base class
class Base:
    def myfun(self):
        print("This is inherited method!")

    # Creating Test class dynamically using


edit
play_arrow

brightness_4

# A Python program to demonstrate working of
# findall()
import re

# A sample text string where regular expression
# is searched.
string = """Hello my Number is 123456789 and 
             my friend's number is 987654321"""

# A sample regular expression to find digits.
regex = '\d+'

match = re.findall(regex, string)
print(match)


# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# initialize the amount variable
marks = 10000

# perform division with 0
a = marks / 0
print(a)

# Driver code
obj1 = Base()
print(obj1.a)

edit
play_arrow

brightness_4
# Program to handle multiple errors with one except statement
try:
    a = 3
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

        # throws NameError if a >= 4
    print
    "Value of b = ", b

# note that braces () are necessary here for multiple exceptions
except(ZeroDivisionError, NameError):
    print
    "\nError Occurred and Handled"


# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


n = int(input())
k = int(input())
print
n, "


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function 
                    passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)


# Uncommenting print(obj1.c) will
# raise an AttributeError


# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class

# Python program to illustrate destructor

class Employee:
    # Initializing
    def __init__(self):
        print('Employee created')
        # Calling destructor

    def __del__(self):
        print("Destructor called")


def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj


print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

# type() method directly
Test = type('Test', (Base,), dict(x="atul", my_method=test_method))
# Print type of Test
print("Type of Test class: ", type(Test))

# Creating instance of Test class
test_obj = Test()
print("Type of test_obj: ", type(test_obj))

# calling inherited method
test_obj.myfun()

# calling Test class method
test_obj.my_method()

# printing variable
print(test_obj.x)
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()


#


# A Python program to demonstrate
# inheritance


# Base class or Parent class
class Child:
    # Constructor
    def __init__(self, name):
        self.name = name
        # To get name

    def getName(self):
        return self.name
        # To check if this person is student

    def isStudent(self):
        return False


# Derived class or Child class
class Student(Child):

    # True is returned
    def isStudent(self):
        return True


import re

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))

# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))
import re

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))

# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))

edit
play_arrow

brightness_4


# Python 3 code to find sum
# of elements in given array
def _sum(arr):
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum = 0

    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i

    return (sum)


# Python 3 code to find sum
# of elements in given array
# driver function
arr = []

# A Python program to demonstrate working of re.match().
import re

# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")

if match != None:

    # We reach here when the expression "([a-zA-Z]+) (\d+)"
    # matches the date string.

    # This will print [14, 21), since it matches at index 14
    # and ends at 21.
    print("Match at index % s, % s" % (match.start(), match.end()))

    # We us group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    # match.group(0) always returns the fully matched string
    # match.group(1) match.group(2), ... return the capture
    # groups in order from left to right in the input string
    # match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print("Full match: % s" % (match.group(0)))

    # So this will print "June"
    print("Month: % s" % (match.group(1)))

    # So this will print "24"
    print("Day: % s" % (match.group(2)))

else:
    print("The regex pattern does not match.")
# input values to list
arr = [12, 3, 4, 15]

# sum() is an inbuilt function in python that adds
# all the elements in list,set and tuples and returns
# the value
ans = sum(arr)

# display sum
print('Sum of the array is ', ans)
# driver function
arr = []
# input values to list
arr = [12, 3, 4, 15]

# calculating length of array
n = len(arr)

ans = _sum(arr)

# display sum
print('Sum of the array is ', ans)


# Python program to
# demonstrate protected members


# Creating a base class
class Base:
    def __init__(self):
        # Protected member
        self._a = 2


class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Outside class will  result in
# AttributeError
print(obj2.a)
# Driver code
# An Object of Child
std = Child("Ram")
print(std.getName(), std.isStudent())


# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"

        edit
        play_arrow

        brightness_4

        # Python program to

        # demonstrate private members

        # Creating a Base class
        class Base:
            def __init__(self):
                self.a = "GeeksforGeeks"
                self.__c = "GeeksforGeeks"

        # Creating a derived class]

        class Derived(Base):
            def __init__(self):
                # Calling constructor of
                # Base class
                Base.__init__(self)
                print("Calling private member of base class: ")
                print(self.__c)

        # Driver code
        obj1 = Base()
        print(obj1.a)

        # Uncommenting print(obj1.c) will
        # raise an AttributeError

        # Uncommenting obj2 = Derived() will
        # also raise an AtrributeError as
        # private member of base class
        # is called inside derived class

        self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived(Base):

    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
# An Object of Student
std = Student("Shivam")
print(std.getName(), std.isStudent())

n = 0
initial_time = time.time()
while n < 10:
    print("Hello world")
    # time.sleep(1)    # this function is used to sleep or stop time according to give seconds
    n = n + 1
print("the time taken in the execution of this program is", time.time() - initial_time)

# now lets check the same condition on for loop
initial_time2 = time.time()
for i in range(50):
    print("hello world")
print("the time taken in executoin of this program is", time.time() - initial_time2)

if initial_time > initial_time2:
    print("for loop is faster")
elif initial_time < initial_time2:
    print("while loop is faster")
else:
    print("both are eqwual ")

curremt_time_now = time.asctime(time.localtime())  # to know the current local time
print(curremt_time_now)


# Password validation in Python
# using naive method

# Function to validate the password
def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

    # Main method


def main():
    passwd = 'Geek12@'

    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")

    # Driver Code


if __name__ == '__main__':
    main()