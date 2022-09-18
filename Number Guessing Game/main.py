import random

"""
 Funtion start() create the magic number, number of attemps, and ask user for input
"""
def start():
    global magic_number
    magic_number = random.randint(1, 100)

    global attempts
    attempts = 0

    print('---------------------------')
    print('Guess a number between 1 and 100')

# Function that checks if player won, if it won, returns True
def check_win(player_guess):
    if player_guess > magic_number:
        print('Too big...')
    elif player_guess < magic_number:
        print('Too small')
    elif player_guess == magic_number:
        return True

start()

# Game loop
while True:
    # Take the player input
    guess = int(input())
    attempts += 1

    if check_win(guess):
        print('You won! - Number of attempts: ' + str(attempts))

        keep_playing = input('Keep playing?(y\\n)')
        # If player want to keep the game, reset the number of attempts
        if keep_playing == 'y':
            attempts = 0
            start()
        # If player don't want to keep playing, quit the game
        elif keep_playing == 'n':
            quit()
