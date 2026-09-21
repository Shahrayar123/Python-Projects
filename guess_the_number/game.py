import random

def guess_game():
    print("Welcome to 'Guess the Number' game!")
    
    # Setting the maximum number of attempts
    max_attempts = 5
    attempts = 0
    
    # The computer chooses a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # The guessing game
    while attempts < max_attempts:
        try:
            # A request from the player to guess a number
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter a number between 1 and 100: "))

            # Checking whether the guess is close to the selected number
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
                break

            attempts += 1

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}.")

if __name__ == "__main__":
    guess_game()
