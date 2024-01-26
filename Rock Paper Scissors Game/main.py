# Rock Paper Scissors game by marsian

import time
import random

# Function to handle the game logic
def game():
    # Prompt the player to choose their move
    print("\n\n\n\n\n\n\n\nDecide your move, enter \"R\" for Rock, \"S\" for Scissors and \"P\"for Paper")
    choice = input()

    # Validate the player's input
    while choice.lower() not in ['r', 's', 'p']:
        print("Invalid choice. Please enter \"R\" for Rock, \"S\" for Scissors, or \"P\" for Paper.")
        choice = input()

    # Convert player's choice to numerical representation
    player_move = 1 if choice.lower() == 'r' else 2 if choice.lower() == 'p' else 3

    # Generate the computer's move
    computer_move = random.choice([1, 2, 3])

    # Convert computer's move to textual representation
    computer_move_text = 'Rock' if computer_move == 1 else 'Paper' if computer_move == 2 else 'Scissors'

    return player_move, computer_move, computer_move_text

# Function to determine the winner of a round
def decisive(player_move, computer_move):
    # Create a winning combinations dictionary
    winning_combinations = {
        (1, 3): player_move,  # Rock beats Scissors
        (2, 1): player_move,  # Paper beats Rock
        (3, 2): player_move,  # Scissors beats Paper
    }

    # Check for a winning combination
    if (player_move, computer_move) in winning_combinations:
        return 1  # Player wins

    # Check for a losing combination
    elif (computer_move, player_move) in winning_combinations:
        return 2  # Computer wins

    # Otherwise, it's a tie
    else:
        return 0

# Function to update the scoreboard
def scoreboard(winner, computer_move_text, computer_score, player_score):
    if winner == 1:
        print("\nCPU won the round by choosing", computer_move_text)
        computer_score += 1
    elif winner == 2:
        print("\nPlayer won the round!")
        player_score += 1

    print("\nSession Score:")
    print("Player:", player_score)
    print("CPU:", computer_score)

    return computer_score, player_score

# Main program
if __name__ == "__main__":
    # Initialize variables
    computer_move = 0
    player_move = 0
    computer_score = 0
    player_score = 0

    while True:
        # Get the player's move and the computer's move
        player_move, computer_move, computer_move_text = game()

        # Determine the winner of the round
        winner = decisive(player_move, computer_move)

        # Handle ties
        while winner == 0:
            print("WoW! A Draw!\nBoth Player and CPU have chosen", computer_move_text)
            print("Let's go again!")

            player_move, computer_move, computer_move_text = game()
            winner = decisive(player_move, computer_move)

        # Display the computer's move
        print("CPU -", computer_move_text)

        # Update the scoreboard
        computer_score, player_score = scoreboard(winner, computer_move_text, computer_score, player_score)

        # Wait for user input before continuing
        input("<<< PRESS ENTER TO CONTINUE >>>")
