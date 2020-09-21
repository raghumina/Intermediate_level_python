# Lambda
# Lambda functions
# lambda functions are generally for convenience
# also known as anonymous func
# they convert program to one liners

# for example
# a normal program

def minus(a,b):
    return a - b

a = 10
b = 5
print(minus(a, b))

# know lets use a lambda function

subs = lambda x,y: x - y
x = 5
y = 5
print(subs(x,y))  # well this is the lambda function or one liner function or anonymous function

# try another example

def list(a):
    return a[1]

a = [[1,23],[23,444],[32323,1]]
a.sort(key=lambda x:x[1])
print(a)