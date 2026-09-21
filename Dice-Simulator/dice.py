import random

def roll_dice():
    print("<<DICE SIMULATOR>>\n")
    number = random.randint(1,6)
    if number == 1:
        print("-----------")
        print("|         |")
        print("|    o    |")
        print("|         |")
        print("-----------")

    elif number == 2:
        print("-----------")
        print("|         |")
        print("| o     o |")
        print("|         |")
        print("-----------")

    elif number == 3:
        print("-----------")
        print("|         |")
        print("| o  o  o |")
        print("|         |")
        print("-----------")

    elif number == 4:
        print("-----------")
        print("| o     o |")
        print("|         |")
        print("| o     o |")
        print("-----------")

    elif number == 5:
        print("-----------")
        print("| o     o |")
        print("|    o    |")
        print("| o     o |")
        print("-----------")

    elif number == 6:
        print("-----------")
        print("| o  o  o |")
        print("|         |")
        print("| o  o  o |")
        print("-----------")
        
    choice = input("\nDo you want to play again? - ")
    if choice.lower() == "n" or choice.lower() == "no":
        exit(0)
    else:
        print("-"*65)
        roll_dice()
        
roll_dice()



