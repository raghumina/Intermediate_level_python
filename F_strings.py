# f strings
# Python f-string is the newest Python syntax to do string formatting. It is available since Python
# Python f-strings provide a faster, more readable, more concise, and less error prone way of formatting strings in Python.
# The f-strings have the f prefix and use {} brackets to evaluate values.

#
# LETS TRY WITH SOME EXAMPLE

name = "messi"
year = "2020"
b = "this is %s%s" % (name, year)
print(b)
# this is a method to update or change a string but it is not so convenient.
# lets do it with another way

palyer = "Neymar"
cup = " cl"
a = "hello player {} {} "  # this a good way to change a list not complicated as former example
b1 = a.format(palyer, cup)
print(b1)

# we can also do this same program as
palyer = "Neymar"
cup = " cl"
a = "hello player {0} {1} "  # by giving it index positions can use it according to our ease
b1 = a.format(palyer, cup)
print(b1)

# f string is like the same above example
# we can also use functions in it
# for example
import datetime
a = "my class starts at"
text = b = f"hello {a} {datetime.datetime.now()}"  # we will use f befrore "" to initiate f string
print(text)

