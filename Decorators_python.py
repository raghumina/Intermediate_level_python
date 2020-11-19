# Decorators
# A decorator takes in a function, adds some functionality and returns it.
# Python has an interesting feature called decorators to add functionality to an existing code.
#
# This is also called metaprogramming because a part of the program tries to modify another part of the program
# at compile time.
'''


def function_1():
    print("hello world")

func = function_1
del function_1

print(func())


# we can put function into an function as an argument
#
def result(func):
    func("helo")

result(print)

#def decoretor_1(func1):
'''
b = [11,13,15,17,19,21]
print(b[::2])

d = {0: 'a', 1: 'b', 2: 'c'}
for x in d.keys():
    print(d[x])





class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))














class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

def addItem(listParam):
    listParam += [1]

mylist = [1, 2, 3, 4]
addItem(mylist)
print(len(mylist))

veggies = ['carrot', 'broccoli', 'potato', 'asparagus']
veggies.insert(veggies.index('broccoli'), 'celery')
print(veggies)

file1 = open("c:\\employee.txt","r")
print(file1)


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()