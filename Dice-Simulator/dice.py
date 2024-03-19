import random       # also do with numpy (from numpy import random)
import sys


# ------------ function definition

def roll_dice():
    number = random.randint(1,6)
    if number == 1:
        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("-----------")

    elif number == 2:
        print("-----------")
        print("|         |")
        print("| 0     0 |")
        print("|         |")
        print("-----------")

    elif number == 3:
        print("-----------")
        print("|    0    |")
        print("|    0    |")
        print("|    0    |")
        print("-----------")

    elif number == 4:
        print("-----------")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("-----------")

    elif number == 5:
        print("-----------")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("-----------")

    elif number == 6:
        print("-----------")
        print("| 0  0  0 |")
        print("|         |")
        print("| 0  0  0 |")
        print("-----------")


print
print("Dice Simulator")
print
x = 'y'
pyver = (sys.version[0])

while x.lower() == "y":
    roll_dice()             # function call
    if pyver == "3":
        choice = input("Do you want to play again (y/n): ")       # choice from user
    else:
        choice = raw_input("Do you want to play again (y/n): ")       # choice from user
    x = choice
    if choice.lower() == "n":
        exit(0)
