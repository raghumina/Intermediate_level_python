# Enumurate function
# - Enumerate() in Python Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

# print(enumerate.__doc__)   # to know about it

# LETS START

list1 = ["messi", "suarez", "mrtinez", "nwymaer"]
# condition is that remove odd players "suarez " and neymar


i = 1
for players in list1:
    if i % 2 is not 0:
        print(players)
        i += 1

# doing it by using enumurate

#for index, name in enumerate(list1):
#    if i%2 == 0:
#        print(name)

from enum import Enum
class Color(Enum):
    RED = 1,
    GREEN = 2,
    BLUE = 3

print(repr(Color.RED))
