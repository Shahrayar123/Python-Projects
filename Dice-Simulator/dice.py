import numpy as np

DICE_FACES = {
    1: """
-----------
|         |
|    0    |
|         |
-----------""",
    2: """
-----------
|         |
| 0     0 |
|         |
-----------""",
    3: """
-----------
|    0    |
|    0    |
|    0    |
-----------""",
    4: """
-----------
| 0     0 |
|         |
| 0     0 |
-----------""",
    5: """
-----------
| 0     0 |
|    0    |
| 0     0 |
-----------""",
    6: """
-----------
| 0  0  0 |
|         |
| 0  0  0 |
-----------"""
}

def roll_dice():
    """Simulate rolling a die and return the result."""
    return np.random.randint(1, 7)

def display_dice(number):
    """Display the dice face for the given number."""
    print(DICE_FACES[number])

def play_game():
    """Main game loop."""
    print("\nDice Simulator\n")
    
    while True:
        result = roll_dice()
        display_dice(result)
        
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()