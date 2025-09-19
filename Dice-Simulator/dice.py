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
    return number

print("                         Dice Simulator                  ")
score=0
x = 'y'
while x.lower() == "y":
   
    rolled_number=roll_dice()     #function called
    score+=rolled_number
    print("Your Score: ",score)
    choice = input("Do you want to play again (y/n): ")       # choice from user

    if choice.lower() == "n":
        print('Your final score: ',score)
        exit(0)
    elif choice.lower()=='y':
        continue
    else:
       print("Invalid Input! Exiting program.")
    exit(0)
