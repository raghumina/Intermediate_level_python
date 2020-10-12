# Classes and Objects in python
# Object Oriented Programming is a way of computer programming
# using the idea of “objects” to represents data and methods.
# A class is a collection of objects or you can say it is a blueprint of objects defining
# the common attributes and behavior.
# Now the question arises, how do you do that?

# Now lets create a class
'''
class student :


    def func(self):
        print("hello")

obj = student()
print(obj.func())
'''

# In easy words class is a template
# Objects are the instances of the classes
# OOPs follows the concepts of DRY that is do not repeat

class Student():
    pass

tom = Student()

tom.name = "Tom"
tom.sec = "A"
tom.standard = 6
tom.roll_no = 22

print(tom.standard)