import random

"""
 Funtion start() create the magic number, number of attemps, and ask user for input
"""
def start():
    global magic_number
    magic_number = random.randint(1, 100)
    print(magic_number)

    global attempts
    attempts = 0

    global total_attempts
    total_attempts = 5 #total number of attempts that player have

    global attempts_left
    attempts_left = total_attempts-attempts

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

    
# function that restarts or end the game according to the user's input
def keep_playing():
    keep_playing = input('Keep playing?(y\\n)')
    # If player want to keep the game, reset the number of attempts
    if keep_playing == 'y':
        attempts = 0
        start()
    # If player don't want to keep playing, quit the game
    elif keep_playing == 'n':
        print("Thanks for playing!!")
        quit()

start()

# Game loop
while True:
    # Take the player input\
    print("attempts left:",attempts_left)
    guess = int(input())
    attempts += 1
    attempts_left = total_attempts-attempts

    if check_win(guess):
        print('You won! - Number of attempts: ' + str(attempts))
        keep_playing()
    if (attempts_left==0):
        print("you lost :(")
        keep_playing()

       
