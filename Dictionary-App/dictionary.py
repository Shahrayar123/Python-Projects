from PyDictionary import PyDictionary
from difflib import get_close_matches

dictionary = PyDictionary()

def check_word(word, action):
    if action == "meaning":
        result = dictionary.meaning(word)
        if result:
            formatted_result = ""
            for part_of_speech, definitions in result.items():
                formatted_result += f"\n{part_of_speech}:\n"
                for i, definition in enumerate(definitions, 1):
                    formatted_result += f"  {i}. {definition}\n"
            return formatted_result.strip()
    elif action == "antonym":
        result = dictionary.antonym(word)
    elif action == "synonym":
        result = dictionary.synonym(word)
    else:
        result = None

    if result:
        if isinstance(result, list):
            return ", ".join(result)
        return result
    else:
        common_words = ["hello", "world", "python", "programming", "dictionary", "language", "computer", "science"]
        close_matches = get_close_matches(word, common_words, n=3, cutoff=0.6)
        if close_matches:
            return f"Word not found. Did you mean: {', '.join(close_matches)}?"
        else:
            return "Word not found and no close matches."

def translate(word, language):
    translation = dictionary.translate(word, language)
    if translation:
        return translation
    else:
        return "Translation not found."

def menu():
    print('''
----------------------------------------------
Enter 1 to check meaning of word
Enter 2 to get antonyms of word
Enter 3 to get synonyms of word
Enter 4 to translate word to other language
Enter 0 to close the dictionary
''')

    choice = input("Enter your choice: ")
    return choice

while True:
    word = input("\nEnter a word: ")
    user_choice = menu()
    
    if user_choice == '0':
        print("Dictionary is closed")
        break
    elif user_choice == '1':
        meaning = check_word(word, "meaning")
        print(meaning)
    elif user_choice == '2':
        antonym = check_word(word, "antonym")
        print(antonym)
    elif user_choice == '3':
        synonym = check_word(word, "synonym")
        print(synonym)
    elif user_choice == '4':
        print('''Enter a language code in which you want to translate the word
Like for URDU language code is ur
For ARABIC language code is ar
For HINDI language code is hi
''')
        lang_choice = input("Enter your choice: ")
        trans = translate(word, lang_choice)
        print(trans)
    else:
        print("Invalid choice!")