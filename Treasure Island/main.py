""" This module help us exit the program """
import sys

print(
    """You are lost in a jungle in search for a treasure.
Your core objective is to find out that treasure.
Now these are the only two ways left for you."""
)
direction = input("Choose 'right' or 'left':  ").lower()
if direction == "right":
    print(
        """This was a good choice. You have come to a river.
But you have to keep patience and wait for the boat to arrive."""
    )
    direction2 = input(
        "Either 'wait' for the boat or 'swim' across the river: "
    ).lower()
    if direction2 == "wait":
        print(
            """Good One. Waiting is a good option. Success come to those
who are patient. Now the boat will soon arrive and you will succeed. """
        )
        direction3 = input(
            """ Now the boat landed you on dry earth and there are
three doors [ White | Black | Yellow ] in front of you choose 
a door and get your treasure: """
        ).lower()
        if direction3 == "white":
            sys.exit("Game Over! You chosed the wrong door. The room is full of fire.")
        elif direction3 == "black":
            sys.exit("You Win! You succeeded in finding the treasure.")
        elif direction3 == "yellow":
            sys.exit("Game Over! There is a lion in the room.")
        else:
            sys.exit("Game Over! You were supposed to choose a door.")

    elif direction2 == "swim":
        sys.exit("Damn! what have you done. Can't you see that aligator. Game Over!")
    else:
        sys.exit("Game Over! Wrong Choice.")
elif direction == "left":
    sys.exit("You feel into a hole. Game Over!")
