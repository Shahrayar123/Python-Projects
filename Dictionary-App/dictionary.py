from PyDictionary import PyDictionary
import difflib

dictionary = PyDictionary()


def check_meaning(word):         # if user want to check meaning of word
    return dictionary.meaning(word)

def get_antonym(word):         # if user want to check antonym of word
    return dictionary.antonym(word)

def get_synonym(word):         # if user want to check synonym of word
    return dictionary.synonym(word)

def translate(word,language):     # if user want to translate word into other language
    return dictionary.translate(word,language)



# Define a function to suggest possible similar words if the entered word does not exist or is misspelled
def suggest_word(word):
    suggested_words = difflib.get_close_matches(word, dictionary.get_words(), n=5, cutoff=0.7)
    if suggested_words:
        print(f"Did you mean one of these words instead: {', '.join(suggested_words)}?")
    else:
        print("Sorry, the word you entered could not be found.")

# Define a function to display a menu and get the user's choice
def menu():
    print('''
----------------------------------------------
Enter 1 to check the meaning of a word
Enter 2 to get antonyms of a word
Enter 3 to get synonyms of a word
Enter 4 to translate a word to another language
Enter 0 to close the dictionary
''')
    choice = int(input("Enter your choice: "))
    return choice

# Main program loop
while True:
    word = input("\nEnter a word: ")
    if not dictionary.meaning(word):
        # If the word does not exist, suggest possible similar words
        suggest_word(word)
    else:
        # If the word exists, display the menu and perform the selected operation
        user_choice = menu()
        match user_choice:
            case 0:
                print("Dictionary is closed")
                exit(0)
            case 1:
                meaning = check_meaning(word)
                print(meaning)
            case 2:
                antonym = get_antonym(word)
                print(antonym)
            case 3:
                synonym = get_synonym(word)
                print(synonym)
            case 4:
                print('''Enter a language code in which you want to translate word
Like for URDU language code is ur
For ARABIC language code is ar
For HINDI language code is hi
''')
                lang_choice = input("Enter your choice: ")
                trans = translate(word, lang_choice)
                print(trans)
            case _:
                print("Invalid choice!")



# Tasks 1–3 have been completed.
#-------------------------------------------------------------

# Next tasks:
# 1- is to make this program in such a way that if word not exist then do something
# 2- also if user enter wrong word by mistake (for example if user want to enter ""happy"" but type "Haappyy") then do something
# 3- task number 2 is with get_close_matches() for difflib library
# 4- then make GUI application of this

#-------------------------------------------------------------


