import random

"""
 Function start() create the magic number, number of attemps, and ask user for input
"""
class starting_value:
    def __init__(self) -> None:
        self.high = 100
        self.low = 1
        self.magic_number = random.randint(1, 100)
        self.attempts = 0

SV_ = starting_value()

def start():
    SV_.magic_number = random.randint(1, 100)
    print('---------------------------')
    print('Guess a number between 1 and 100')

# Function that checks if player won, if it won, returns True
def check_win(player_guess):
    if player_guess > SV_.magic_number:

        if player_guess < SV_.high:
            SV_.high = player_guess
        print('Too big...')
        print(f'it is between {SV_.low} and {SV_.high}')

    elif player_guess < SV_.magic_number:

        if player_guess > SV_.low:
            SV_.low = player_guess
        print('Too small')
        print(f'it is between {SV_.low} and {SV_.high}')

    elif player_guess == SV_.magic_number:
        return True
    

start()

# Game loop
while True:
    # Take the player input
    guess = int(input())
    SV_.attempts += 1
    
    if check_win(guess):
        print('You won! - Number of attempts: ' + str(SV_.attempts))

        keep_playing = input('Keep playing?(y\\n)')
        # If player want to keep the game, reset the number of attempts
        if keep_playing == 'y':
            SV_.attempts = 0
            SV_.high = 100
            SV_.low = 1
            start()
        # If player don't want to keep playing, quit the game
        elif keep_playing == 'n':
            quit()
