import random

"""
 Funtion start() create the magic number, number of attemps, and ask user for input
"""

attempts = 0
magic_number = 0

#user's choice
def choice ():
    print('what you want to play ?\n 1 for number guess.\n 2 for word guess.')
    user = int(input('>> '))
    if user == 1:
        print('____________GUESS THE NUMBER____________')
        start()
    elif user == 2:
        print('---------------GUESS THE WORD-------------')
        StringGame()

def StringGame():
      words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'morning','hello','evening','night','day','smooth','torch','good','bad','beautiful','ugly','messy','clean','house','home','garden','building','java','nice','adjust','congrates','then']
      word = random.choice(words)
      print("Guess the characters")
      guesses = ''
      turns = 14
      while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("You Won the game.")
            print("The word is: ", word)
            choice()
        print()
        guesschar = input("guess a character:")
        guesses += guesschar
        if guesschar not in word:
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You Lost the game.")
                choice()

def start():
    global magic_number
    magic_number = random.randint(1, 100)
    guess = 0
    global attempts
    attempts = 0

    print('---------------------------')
    print('Guess a number between 1 and 100')
    check_win(guess)
# Function that checks if player won, if it won, returns True
def check_win(player_guess):
    if player_guess > magic_number:
        print('Too big...')
    elif player_guess < magic_number:
        print('Too small')
    elif player_guess == magic_number:
        return True
    # Game loop
    while True:
        # Take the player input
        guess = int(input())
        global attempts
        attempts += 1

        if check_win(guess):
            print('You won! - Number of attempts: ' + str(attempts))

            keep_playing = input('Keep playing?(y\\n)')
            # If player want to keep the game, reset the number of attempts
            if keep_playing == 'y':
                attempts = 0
                choice()
            # If player don't want to keep playing, quit the game
            elif keep_playing == 'n':
                quit()
choice()
