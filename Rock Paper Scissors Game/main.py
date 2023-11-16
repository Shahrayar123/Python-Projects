#Grab randomizer to create computer's choice
import random

#Function to take user's selection as int and return a win, loss or draw condition.
def rps(user_choice):
    choices = ["paper", "scissors", "rock"]
#Exception handler
    if user_choice < 0 or user_choice > 2:
        raise ValueError("Invalid selection. Please enter a number between 0 and 2.")
#variable assignment for passing cpu random selection and user selection into a list 
    cpu_choice = random.randint(0, 2)
    user_selection = choices[user_choice]
    computer_selection = choices[cpu_choice]

#Comparator
    if user_selection == computer_selection:
        return "It's a tie!"
    elif (user_selection == "paper" and computer_selection == "rock") or (user_selection == "scissors" and computer_selection == "paper") or (user_selection == "rock" and computer_selection == "scissors"):
        winning_statement = f"You win! User chose {user_selection}, computer chose {computer_selection}."
        return winning_statement
    else:
        losing_statement = f"You lose! User chose {user_selection}, computer chose {computer_selection}."
        return losing_statement

# Example usage
user_input = int(input("Please select paper(0), scissors(1) or rock (2): "))
game_result = rps(user_input)
print(game_result)
