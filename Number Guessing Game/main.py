import random

def start():
    """
    Creates the magic number, number of attempts, and asks the user for input.
    """
    global magic_number, attempts
    magic_number = choose_difficulty()
    attempts = 0
    print('---------------------------')
    print('Guess the magic number!')
    print('Try to guess the number in as few attempts as possible.')

def choose_difficulty():
    """
    Allows the user to select the difficulty level and returns the corresponding range for the magic number.
    """
    print("Choose difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    while True:
        level = input("Enter 1, 2, or 3: ")
        if level == '1':
            return random.randint(1, 50)
        elif level == '2':
            return random.randint(1, 100)
        elif level == '3':
            return random.randint(1, 200)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def check_win(player_guess):
    """
    Checks if the player’s guess is correct, too high, or too low.
    """
    if player_guess > magic_number:
        print('Too high! Try a smaller number.')
    elif player_guess < magic_number:
        print('Too low! Try a larger number.')
    elif player_guess == magic_number:
        return True

def play_game():
    """
    Main game loop that starts the game, processes user input, and checks for win conditions.
    """
    global attempts
    start()

    while True:
        try:
            guess = int(input('Enter your guess: '))
            if guess < 1 or guess > 200:
                print("Please enter a number between 1 and 200.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if check_win(guess):
            print(f'Congratulations! You guessed the number in {attempts} attempts.')
            keep_playing = input('Would you like to play again? (y/n): ')
            if keep_playing.lower() == 'y':
                play_game()
            elif keep_playing.lower() == 'n':
                print("Thanks for playing! Have a great day!")
                break
            else:
                print("Invalid input. Exiting the game.")
                break

play_game()
