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
