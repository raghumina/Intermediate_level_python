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


# Driver code
# An Object of Child
std = Child("Ram")
print(std.getName(), std.isStudent())

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
