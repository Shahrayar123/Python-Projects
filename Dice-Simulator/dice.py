import random       # also do with numpy (from numpy import random)

# create dictionary with all the dice ACSII art 
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
    ),
}


# ------------ function definition

def roll_dice(num_of_dice):
    roll_results = []
    for _ in range(num_of_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

def combine_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(dice_vis[value])
    

    dice_faces_rows = []
    for row_idx in range(5):
        row_components = []
        for face_index in dice_faces:
            row_components.append(face_index[row_idx])
        row_string = "    ".join(row_components)
        dice_faces_rows.append(row_string)

    return dice_faces_rows


#------------- main block

print("                         Dics Simulator                  ")
num_dice_input = input("How many dice do you want to use? (choose 1-5) ")

# roll the dice chosen number of times
all_rolls = roll_dice(int(num_dice_input))

# print all faces for chosen numbers in one line
for i in combine_faces(all_rolls):
    print(i)


"""
x = 'y'
while x.lower() == "y":
    roll_dice()             # function call
    choice = input("Do you want to play again (y/n): ")       # choice from user

    if choice.lower() == "n":
        exit(0)
        
"""




