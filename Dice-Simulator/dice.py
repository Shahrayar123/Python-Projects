import random       # also do with numpy (from numpy import random)

# create dictionary with all the dice ACSII art (visuals for short)
dice_vis = {
    1: (
        "-----------",
        "|         |",
        "|    0    |",
        "|         |",
        "-----------"
        ),
    2: (
        "-----------",
        "| 0       |",
        "|         |",
        "|       0 |",
        "-----------"
        ),
    3: (
        "-----------",
        "|       0 |",
        "|    0    |",
        "| 0       |",
        "-----------"
        ),
    4: (
        "-----------",
        "| 0     0 |",
        "|         |",
        "| 0     0 |",
        "-----------"
        ),
    5: (
        "-----------",
        "| 0     0 |",
        "|    0    |",
        "| 0     0 |",
        "-----------"
        ),
    6: (
        "-----------",
        "| 0     0 |",
        "| 0     0 |",
        "| 0     0 |",
        "-----------"
        )
}


# ------------ function definition

# number of dice to roll -> list with the resulting rolls
def roll_dice(num_of_dice:int):
    roll_results = []
    for _ in range(num_of_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

# list of rolls -> string that combines all the dice visuals into one string to be printed
def combine_faces(dice_values:list):
    # first get visuals individually 
    dice_faces = []
    for value in dice_values:
        dice_faces.append(dice_vis[value])
    
    # then combine into one
    dice_faces_rows = []
    for row_idx in range(5):
        row_components = []
        for face_index in dice_faces:
            row_components.append(face_index[row_idx])
        row_string = "    ".join(row_components)
        dice_faces_rows.append(row_string)

    return dice_faces_rows


#------------- main block

#setup for couniuous rolling
roll = True

# initial print
print("\n" + " DICE SIMULATOR ".center(60, "#") + "\n")

# user input
num_dice_input = None
# check if the input is a number form 1-10, otherwise ask to re-enter
while num_dice_input is None:
    num_dice_input = input("How many dice do you want to use? (choose 1-10) ")
    if num_dice_input in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}:
        num_dice_input = int(num_dice_input)
    else:
        print("Incorrect input. Please re-enter a number from 1 to 10.")
        num_dice_input = None

# user can roll till satisfaction
while roll:
    # roll the dice chosen number of times
    all_rolls = roll_dice(int(num_dice_input))

    # print all faces for chosen numbers in one line
    print(" RESULT ".center(60, "~"))
    for i in combine_faces(all_rolls):
        print(i)

    next_roll = input("Do you want to roll again? (y/n): ")
    if next_roll.lower() == "n":
        roll = False
