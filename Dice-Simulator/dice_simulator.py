import random


def roll_dice():
    number = random.randint(1, 6)
    top_bottom = "-----------"
    empty = "|         |"
    left = "| 0       |"
    center = "|    0    |"
    right = "|       0 |"
    both = "| 0     0 |"
    triple_left_right = "|0  0  0  |"
    triple_all = "|0 0 0 0 0|"

    if number == 1:
        faces = [top_bottom, empty, center, empty, top_bottom]
    elif number == 2:
        faces = [top_bottom, empty, both, empty, top_bottom]
    elif number == 3:
        faces = [top_bottom, left, center, right, top_bottom]
    elif number == 4:
        faces = [top_bottom, both, empty, both, top_bottom]
    elif number == 5:
        faces = [top_bottom, both, center, both, top_bottom]
    elif number == 6:
        faces = [top_bottom, triple_left_right, empty, triple_left_right, top_bottom]

    for face in faces:
        print(face)
    return number


def main():
    print("Dice Simulator")
    score = 0
    rounds = 0
    while True:
        rounds += 1
        score += roll_dice()
        x = input("Do you want to play again (y/n)? ").strip().lower()
        if x not in ('y', 'n'):
            print("Invalid input, please enter 'y' for yes or 'n' for no.")
        if x == 'n':
            print(f"Thanks for playing! You played {rounds} rounds with a total score of {score}.")
            break


if __name__ == "__main__":
    main()


