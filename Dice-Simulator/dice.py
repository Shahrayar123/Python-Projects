import random       # also do with numpy (from numpy import random)


# ------------ function definition

def roll_dice():
    number = random.randint(1,6)
    if number == 1:
        print("""
        -----------      
        |         |
        |    0    |
        |         |
        -----------
        """)

    elif number == 2:
        print("""
        -----------      
        |         |
        | 0     0 |
        |         |
        -----------
        """)

    elif number == 3:
        print("""
        -----------      
        |    0    |
        |    0    |
        |    0    |
        -----------
        """)

    elif number == 4:
        print("""
        -----------      
        | 0     0 |
        |         |
        | 0     0 |
        -----------
        """)

    elif number == 5:
        print("""
        -----------      
        | 0     0 |
        |    0    |
        | 0     0 |
        -----------
        """)
    
    elif number == 6:
        print("""
        -----------      
        | 0     0 |
        | 0     0 |
        | 0     0 |
        -----------
        """)


print("                         Dice Simulator                  ")
x = 'y'
while x.lower() == "y":
    roll_dice()             # function call
    choice = input("Do you want to play again (y/n): ")       # choice from user

    if choice.lower() == "n":
        exit(0)




