# IMPORT ALL LIBRARIES
import requests
import random
from lxml import etree

alphabetChoice = random.choice(["a","b","c","d","e","f","g","h","i"])
columnChoice = random.choice(range(1, 3))
wordChoice = random.choice(range(1, 10))

def checkName(name):
    if name == "":
        print("Sorry, you did not enter your name")
        return 0
    else:
        print("\n--------------------------------------\n")
        return 1
    
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
    # print(WORD)
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    chance = 10
    guess_made = ""
    attemps = [""*26]

    while len(word) > 0:
        main = ""
        for letter in word:
            if letter in guess_made:
                main += letter
            else:
                main = main +"_"+" "

        if main == word:
            print("The word is: "+ main)
            print("Congratulations, you won!")
            break

        print(f"Guess the word {main}")
        guess = input("\n")

        while guess in attemps:
            print("You've already tried this letter, make another guess")
            guess = input("\n")
            if guess not in attemps:
                break
        attemps.append(guess)

        if guess in alphabets:
            guess_made = guess_made + guess
        else:
            guess = input("Enter a valid character:\n")

        if guess not in word:
            chance -= 1

            if chance == 9:
                print("9 turns left")
                print("\n---------------------------- ")
                print("      (      ")

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
                print("last breath...")
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


name = input("Hey there! What is your name: ")

if checkName(name):
    print(name+" lets play a game")
    hangman()
else:
    pass