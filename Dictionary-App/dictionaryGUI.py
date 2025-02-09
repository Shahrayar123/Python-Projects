import tkinter as tk
from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()

# Function to check the meaning of a word
def check_meaning(word):
    meaning = dictionary.meaning(word)
    if meaning:
        return "\n".join([f"{part}: {', '.join(definitions)}" for part, definitions in meaning.items()])
    else:
        return "Meaning not found."

# Function to get antonyms of a word
def get_antonym(word):
    antonyms = dictionary.antonym(word)
    if antonyms:
        return ", ".join(antonyms)
    else:
        return "Antonyms not found."

# Function to get synonyms of a word
def get_synonym(word):
    synonyms = dictionary.synonym(word)
    if synonyms:
        return ", ".join(synonyms)
    else:
        return "Synonyms not found."

# Function to translate a word to another language
def translate(word, language):
    translation = dictionary.translate(word, language)
    if translation:
        return translation
    else:
        return f"Translation to {language} not found."

# Function to update the response based on checkbox and dropdown selections
def update_response():
    selected_word = entry.get()
    meaning_text.delete(1.0, tk.END)  # Clear previous meaning
    results_text.delete(1.0, tk.END)  # Clear previous results
    if selected_word:
        meaning = check_meaning(selected_word)
        meaning_text.insert(tk.END, f"Meaning:\n{meaning}\n")

        if antonyms_var.get():
            antonyms = get_antonym(selected_word)
            results_text.insert(tk.END, f"Antonyms: {antonyms}\n")

        if synonyms_var.get():
            synonyms = get_synonym(selected_word)
            results_text.insert(tk.END, f"Synonyms: {synonyms}\n")

        if translation_var.get():
            lang_choice = translation_var.get()
            trans = translate(selected_word, lang_choice)
            results_text.insert(tk.END, f"Translation ({lang_choice}): {trans}\n")

# Function to display the initial meaning
def display_initial_meaning(event):
    selected_word = entry.get()
    meaning_text.delete(1.0, tk.END)  # Clear previous meaning
    if selected_word:
        meaning = check_meaning(selected_word)
        meaning_text.insert(tk.END, f"Meaning:\n{meaning}\n")

# Creating main tkinter window
mainWindow = tk.Tk()
mainWindow.title('Dictionary')
mainWindow.geometry("800x500")

# Checkbox widgets
antonyms_var = tk.BooleanVar()
antonyms = Checkbutton(mainWindow, text="Antonyms", variable=antonyms_var)
antonyms.grid(row=3, column=0, sticky=W, columnspan=2,padx=20)

synonyms_var = tk.BooleanVar()
synonyms = Checkbutton(mainWindow, text="Synonyms", variable=synonyms_var)
synonyms.grid(row=4, column=0, sticky=W, columnspan=2,padx=20)

# Label for the Translation dropdown menu
translation_label = Label(mainWindow, text="Translation:")
translation_label.grid(row=5, column=0, sticky=W, padx=20)

# Translation dropdown menu
languages = ["","ur", "ar", "hi"]  # Add your language codes here
translation_var = tk.StringVar()
translation_var.set(languages[0])  # Set the default language
translation_menu = OptionMenu(mainWindow, translation_var, *languages)
translation_menu.grid(row=5, column=1, sticky=W)


# Entry widget with placeholder text
placeholder_text = ""
entry = Entry(mainWindow, fg="gray")
entry.insert(0, placeholder_text)
entry.bind("<FocusIn>", display_initial_meaning)
entry.bind("<FocusOut>", display_initial_meaning)
entry.grid(row=0, column=0,sticky=W, pady=10, padx=20)

# Text widget for displaying meaning
meaning_text = Text(mainWindow, height=10, width=40)
meaning_text.grid(column=0, columnspan=2, padx=20, pady=10)

# Text widget for displaying results
results_text = Text(mainWindow, height=10, width=40)
results_text.grid(row=6, column=6, columnspan=2, padx=20, pady=10)

# Search button
def display_response():
    update_response()
searchBtn = Button(mainWindow, text="Search", padx=5, command=display_response)
searchBtn.grid(row=1, column=0, sticky=W, pady=2, padx=20)

# Infinite loop which can be terminated by keyboard or mouse interrupt
mainWindow.mainloop()
