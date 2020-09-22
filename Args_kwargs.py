# args and kwargs
# args , *args: The special syntax *args in function definitions in python is used to pass a variable number of
# arguments to a function. It is used to pass a non-key worded, variable-length argument list.

# lets start:
#

#def names(a,b,c,d):
 #   print(a,b,c,d)

#names("tom","Jerry","kimi","tofa")

# but in this simple functions we cant add or remove the numbewr of arguments in the function
# So this is not suitable for big programs where input can be more than expectations so we use *arg for this

def arg(*args):
    print(args)
num = [1,2,3,4,5,6,7]
arg(*num)
num.append(22)
arg(*num)           # so without any error it adds or update the list
num.pop()
arg(*num)


