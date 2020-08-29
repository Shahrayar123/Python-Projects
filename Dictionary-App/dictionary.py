from PyDictionary import PyDictionary

dictionary = PyDictionary()


def check_meaning(word):         # if user want to check meaning of word
    return dictionary.meaning(word)

def check_antonym(word):         # if user want to check antonym of word
    return dictionary.antonym(word)

def check_synonym(word):         # if user want to check synonym of word
    return dictionary.synonym(word)

def translate(word,language):     # if user want to translate word into other language
    return dictionary.translate(word,language)



def menu():
    print("\n----------------------------------------------")
    print("Enter 1 to check meaning of word")
    print("Enter 2 to check antonym of word")
    print("Enter 3 to check synonym of word")
    print("Enter 4 to translate word to other language")
    print("Enter 0 to the close dictionary")
    print()

    choice = int(input("Enter your choice: "))

    return choice


while(True):
    word = input("\nEnter a word: ")
    user_choice = menu()

    if user_choice == 0:
        print("Dictionary is closed")
        exit(0)

    elif user_choice == 1:
        meaning = check_meaning(word)
        print(meaning)

    elif user_choice == 2:
        antonym = check_antonym(word)
        print(antonym)

    elif user_choice == 3:
        synonym = check_synonym(word)
        print(synonym)

    elif user_choice == 4:
        print("Enter a language code in which you want to translate word")
        print("Like for URDU language code is ur ")
        print("For ARABIC language code is ar ")
        print("For HINDI language code is hi ")

        lang_choice = input("Enter your choice: ")
        trans = translate(word,lang_choice)
        print(trans)

    else:
        print("Invalid choice!")

#-------------------------------------------------------------

# Next tasks:
# 1- is to make this program in such a way that if word not exist then do something
# 2- also if user enter wrong word by mistake (for example if user want to enter ""happy"" but type "Haappyy") then do something
# 3- task number 2 is with get_close_matches() for difflib library
# 4- then make GUI application of this

#-------------------------------------------------------------


