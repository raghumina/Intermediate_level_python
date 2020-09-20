# Recursion
# Recursion is a method of programming or coding a problem, in which a function calls itself one or more times in its body.


# lets start with an example
#
# factorial of a nmumber
def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
        return fact

num = int(input("Enter a number: "))
print(factorial(num))