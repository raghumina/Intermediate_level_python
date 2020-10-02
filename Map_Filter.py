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

# lets do it with another way

def square(a):
  return a*a

def cube(a):
  return a*a*a

num = [square, cube]
for i in range(5):
  val = list(map(lambda x:x(i), num))
  print(val)
'''

# filter function
# it filter the list or other data types according to our choice and needs
# The filter() method filters the given sequence with the help of a function
# that tests each element in the sequence to be true or not.

number = [1,2,3,4,5,6,7,8,9,0,10]
def is_greater(number):
  return number>5

filter_1 = list(filter(is_greater, number))
print(filter_1)






