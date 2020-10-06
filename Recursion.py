# Recursion
# Recursion is a method of programming or coding a problem, in which a function calls itself one or more times in its body.

'''
# lets start with an example
#
# factorial of a nmumber
#
def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n - 1 )

n = int(input())
print(factorial(n))

# so this is a factorial program with recursion
'''


# the iterative way of solving this problem is

def facto(n):
    f = 1
    for i in range(1, n + 1):
        fac = f * i
        return fac


n = int(input())
print(facto(n))

# Python3 code to demonstrate working of
# Convert String to unicode characters
# using join() + format() + ord()
import re

# initializing string
test_str = 'ATGC'

# printing original String
print("The original string is : " + str(test_str))

# using format to perform required formatting
res = ''.join(r'\u{:04X}'.format(ord(chr)) for chr in test_str)

# printing result
print("The unicode converted String : " + str(res))