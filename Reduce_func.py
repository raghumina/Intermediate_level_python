# Reduce in python
#
# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements
# mentioned in the sequence passed along.This function is defined in “functools” module.

from functools import reduce
num = [1,2,3,4,5,65,67]
number = reduce(lambda x, y: x + y , num)
print(number)

# another example
# initializing list
import functools 
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))