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
