# Problem
# # game: Stone Paper Secissor
import random

'''
list = ["Stone","Paper","Scissor"]
machine_choice = random.choice(list)
#print(choice)
user1 = str(input("Please enter Stone or Paper or Scissor: " ))
#user1 = user.upper()
if user1 == "Stone" and machine_choice == "Stone":
    print("Game tied")
elif user1 == "Stone" and machine_choice == "Paper":
    print("machine won")
elif user1 == "Stone" and machine_choice == "Scissor":
    print("User won")
elif user1 == "Paper" and machine_choice == "Paper":
    print("Game tied")
elif user1 == "Paper" and machine_choice == "Stone":
    print("User won")
elif user1 == "Paper" and machine_choice == "Scissor":
    print("Machine won")
elif user1 == "Scissor" and machine_choice == "Stone":
    print("Machine won")
elif user1 == "Scissor" and machine_choice == "Paper":
    print("User won")
elif user1 == "Scissor" and machine_choice == "Scissor":
    print("Game tied")
else:
    print("Please enter value correctly")
 '''
# lets do it with a function:
# or in a better way

print("This is a Stone Paper Secissor game")
print("In this game you will play with computer")
print("Rules are simple ")

print("Lets Play")
import random

chance = 0


def chances():
    while chance >= 10:
        print("Uou loose ")

    #  print("You LOOSE")


def user_input(user1):
    if user1 == "Stone" and machine_choice == "Stone":
        return "Game tied"

    elif user1 == "Stone" and machine_choice == "Paper":
        return "machine won"

    elif user1 == "Stone" and machine_choice == "Scissor":
        return "User won"

    elif user1 == "Paper" and machine_choice == "Paper":
        return "Game tied"

    elif user1 == "Paper" and machine_choice == "Stone":
        return "User won"

    elif user1 == "Paper" and machine_choice == "Scissor":
        return "Machine won"

    elif user1 == "Scissor" and machine_choice == "Stone":
        return "Machine won"

    elif user1 == "Scissor" and machine_choice == "Paper":
        return "User won"
    
    elif user1 == "Scissor" and machine_choice == "Scissor":
        return "Game tied"
    else:
        print("Please enter value correctly")


user_choice = ["Stone", "Paper", "Scissor"]
machine_choice = random.choice(user_choice)
user1 = input("Enter your choice here: Stone, Paper, Scissor: ")
print(user_input(user1))
