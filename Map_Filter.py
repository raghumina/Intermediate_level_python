# Map filter and reduce
# Map function applies a functiion on whole list
# The map() function executes a specified function for each item in an iterable. The item
# is sent to the function as a parameter.
'''
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
print(list(x))

# USING THIS WITH LAMBDA

list1 = [2,2,2,2,2,2,2,2,2,2]
square = list(map(lambda x: x*x, list1))
print(square)
'''
# lets do it with another way

def square(a):
  return a*a

def cube(a):
  return a*a*a

num = [square, cube]
for i in range(5):
  val = list(map(lambda x:x(i), num))
  print(val)



