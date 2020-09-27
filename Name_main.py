# if_name == _main_
# this is used when we import a module or file in another file but we dont want the other lines or execution of code
# other then required one then i will put that extra code in _main_
# for example

def sum(n,n2):
    return n + n2 + 10

print(sum(2,2))
print("hello0")
###### when i import this module t6o other file and run the function then the printstatement of this module will aslo get
# returned in that respective file
# but to stop that we will use _main_ command



def sum(n,n2):
    return n + n2 + 10
if __name__ == '__main__':   # so this coomand will stop this commands from running in other module or file
    print(sum(2,2))
    print("hello0")