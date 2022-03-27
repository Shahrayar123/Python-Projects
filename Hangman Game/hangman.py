import random

words = ["pencil","pen","superman","glasses","mobile","calculator","laptop","book","person","animal","john","joey","joseph","joe","johnathan","stool","chair","bar","pub","america","germany","china","india","japan","russia","ukraine","africa","canada","singapore","north america","south america","brazil","amazon river","chile","chili pepper","jalapeno","pepper","seasoning","american","japanese","chinese","german","canadian"]

def hangman():
    WORD = random.choice(words)
    # print(WORD)
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    chance = 10
    guess_made = ""

    while len(WORD) > 0:
        main = ""
        for letter in WORD:
            if letter in guess_made:
                main += letter
            else:
                main = main +"_"+" "

        if main == WORD:
            print("Letter is: "+ main)
            print("You win! ")
            break

        guess = input("Guess the word "+ main)

        if guess in alphabets:
            guess_made = guess_made + guess
        else:
            guess = input("Enter the valid character: ")

        if guess not in WORD:
            chance -= 1

            if chance == 9:
                print("9 turns left")
                print("\n---------------------------- ")

            if chance == 8:
                print("9 turns left")
                print("\n---------------------------- ")
                print("      O     ")
            if chance == 7:
                print("7 turns left")
                print("\n---------------------------- ")
                print("      O     ")
                print("      |      ")
            if chance == 6:
                print("6 turns left")
                print("\n---------------------------- ")
                print("      O     ")
                print("      |      ")
                print("     /       ")
            if chance == 5:
                print("5 turns left")
                print("\n---------------------------- ")
                print("      O     ")
                print("      |      ")
                print("     / \     ")
            if chance == 4:
                print("4 turns left")
                print("\n---------------------------- ")
                print("     \O     ")
                print("      |      ")
                print("     / \     ")
            if chance == 3:
                print("3 turns left")
                print("\n---------------------------- ")
                print("     \O/   ")
                print("      |      ")
                print("     / \     ")
            if chance == 2:
                print("2 turns left")
                print("\n---------------------------- ")
                print("     \O/  |  ")
                print("      |      ")
                print("     / \     ")
            if chance == 1:
                print("1 turns left")
                print("last breating...")
                print("\n---------------------------- ")
                print("     \O/ __|  ")
                print("      |      ")
                print("     / \     ")

            if chance == 0:
                print("You loss that man")
                print("Game Over")
                print("      O____|  ")
                print("     /|\      ")
                print("     / \     ")

                break



name = input("Hey there! What is your name: ")
print(name+" lets play a game")
print("\n--------------------------------------\n")
hangman()
