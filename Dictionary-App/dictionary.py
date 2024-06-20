from PyDictionary import PyDictionary
from difflib import get_close_matches

dictionary = PyDictionary()

def check_meaning(word):
    try:
        meaning = dictionary.meaning(word)
        return meaning
    except KeyError:
        suggestions = get_close_matches(word, dictionary.synonym(word))
        if suggestions:
            return f"Word not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return "Word not found."

def get_antonym(word):
    try:
        antonym = dictionary.antonym(word)
        return antonym
    except KeyError:
        suggestions = get_close_matches(word, dictionary.synonym(word))
        if suggestions:
            return f"Word not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return "Word not found."

def get_synonym(word):
    try:
        synonym = dictionary.synonym(word)
        return synonym
    except KeyError:
        suggestions = get_close_matches(word, dictionary.synonym(word))
        if suggestions:
            return f"Word not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return "Word not found."

def translate(word, language):
    try:
        translation = dictionary.translate(word, language)
        return translation
    except KeyError:
        suggestions = get_close_matches(word, dictionary.synonym(word))
        if suggestions:
            return f"Word not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return "Word not found."

def menu():
    print('''
----------------------------------------------
Enter 1 to check the meaning of a word
Enter 2 to get antonyms of a word
Enter 3 to get synonyms of a word
Enter 4 to translate a word to another language
Enter 0 to close the dictionary
''')

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [0, 1, 2, 3, 4]:
                return choice
            else:
                print("Invalid choice! Please enter a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number.")

while True:
    word = input("\nEnter a word: ")
    user_choice = menu()
    if user_choice == 0:
        print("Dictionary is closed.")
        break
    else:
        if user_choice == 1:
            result = check_meaning(word)
        elif user_choice == 2:
            result = get_antonym(word)
        elif user_choice == 3:
            result = get_synonym(word)
        else:
            print('''Enter a language code in which you want to translate the word.
Like for URDU, the language code is 'ur'.
For ARABIC, the language code is 'ar'.
For HINDI, the language code is 'hi'.
''')
            lang_choice = input("Enter your choice: ")
            result = translate(word, lang_choice)
        print(result)
