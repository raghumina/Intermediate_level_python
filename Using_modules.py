# Modules in python
# Modules in Python are simply Python files with a .py extension. The name of the module will be the name of the file.
# A Python module can have a set of functions, classes or variables defined and implemented.

# modules are different form packages
# modules are for specific task
# whereas packages are collection of modules which can lend a hand in diff diff tasks

# lets try
import random  # random module to generate random numbers
               # by pressing cntrl and clicking on modules we can open its file

random_num = random.randint(1,1000)
#for random_num in range(1000):
#print(random_num)                 # each time it will  gives a random number

rand = random.random() * 10
#print(rand)

# this can also be used in getting random values form a list
#list = ["messi","suarez","kaka","ronaldo","neymar"]
#choice = random.choice(list)
#print(choice)

# another module
import csv
#csv1 = open("Movie_regression.csv")
#csv12 = csv1.read()
#print(csv12)
'''
import csv

with open('employee.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    
    '''
