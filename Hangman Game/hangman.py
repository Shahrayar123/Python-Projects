# IMPORT ALL LIBRARIES
import requests
import random
from lxml import etree

# OBTAIN RANDOM CHOICES
alphabetChoice = random.choice(["a","b","c","d","e","f","g","h","i"])
columnChoice = random.choice(range(1, 3))
wordChoice = random.choice(range(1, 10))

# FUNCTION TO CHECK NAME IF EMPTY OR NOT
def checkName(name):
    if name == "":
        print("Sorry, you did not enter your name")
        return 0
    else:
        print("\n--------------------------------------\n")
        return 1

# MAIN FUNCTION OF GAME
def hangman():
    # Define the URL and XPath
    url = f"https://randomword.com/words/{alphabetChoice}.html"
    xpath = f"/html/body/div[1]/div[2]/div/div/div[1]/div[2]/ul[1]/li[{wordChoice}]"

    # Send a GET request to the website
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content
    tree = etree.HTML(html_content)

    # Extract the desired element using the XPath
    word = tree.xpath(xpath)[0].text.strip()
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    chance = 10
    guess_made = ""

    while len(word) > 0:
        main = ""
        for letter in word:
            if letter in guess_made:
                main += letter
            else:
                main = main +"_"+" "

        if main == word:
            print("Letter is: "+ main)
            print("You win! ")
            break

        print(f"Guess the word {main}")
        guess = input("\n")

        if guess in alphabets:
            guess_made = guess_made + guess
        else:
            guess = input("Enter the valid character:\n")

        if guess not in word:
            print(word)
            chance -= 1

            if chance == 9:
                print("9 turns left")
                print("\n---------------------------- ")

            if chance == 8:
                print("8 turns left")
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
                print(f"You loss that man. The answer was {word}")
                print("Game Over")
                print("      O____|  ")
                print("     /|\      ")
                print("     / \     ")

                break

# START PROGRAM HERE

name = input("Hey there! What is your name: ")

if checkName(name):
    print(name+" lets play a game")
    hangman()
else:
    pass