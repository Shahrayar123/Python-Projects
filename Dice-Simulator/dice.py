import random       # also do with numpy (from numpy import random)


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


print("                         Dice Simulator                         ")
roll_dice() 
while True:
          # function call
    choice = input("Do you want to play again (y/n): ")       # choice from user

    if choice.lower() == "n":
        exit(0)
    elif choice.lower() == "y":
        roll_dice() 
    else:
        print("Invalid input")




