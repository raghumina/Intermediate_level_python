# Map filter and reduce
# Map function applies a functiion on whole list
# The map() function executes a specified function for each item in an iterable. The item
# is sent to the function as a parameter.

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
print(list(x))

