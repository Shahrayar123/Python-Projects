import random 

def diceRoller():
    result = random.randint(0,5)+1
    return(result)

roll = diceRoller()
print(roll)

if(roll == 1):
    print("-----------\n|     |\n|  0  |\n|     |\n-----------")
elif(roll == 2):
    print("-----------\n|     |\n|0   0|\n|     |\n-----------")
elif(roll == 3):
    print("-----------\n|     |\n|0 0 0|\n|     |\n-----------")
elif(roll == 4):
    print("-----------\n|     |\n|00 00|\n|     |\n-----------")
elif(roll == 5):
    print("-----------\n|     |\n|00000|\n|     |\n-----------")
elif(roll == 6):
    print("-----------\n|     |\n|   6 |\n|     |\n-----------")


"""
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


print("                         Dics Simulator                  ")
x = 'y'
while x.lower() == "y":
    roll_dice()             # function call
    choice = input("Do you want to play again (y/n): ")       # choice from user"""

    if choice.lower() == "n":
        exit(0)




