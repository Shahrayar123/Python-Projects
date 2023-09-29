import tkinter as tk
from tkinter import *

# creating main tkinter window
mainWindow = tk.Tk()
mainWindow.title('Dictionary')
mainWindow.geometry("600x400")

#search button
global results
results = " "

# on button press trigger response
def displayResponse():
    results="response is here"
    return results


searchBtn = Button(mainWindow, text = "Search",padx=5, command= displayResponse())
searchBtn.grid(row=1, column=0,sticky=W,pady=2,padx=20)

# checkbox widget
antonyms = Checkbutton(mainWindow, text = "Antonyms")
antonyms.grid(row = 3, column = 0, sticky = W, columnspan = 2)

synonyms = Checkbutton(mainWindow, text = "Synonyms")
synonyms.grid(row = 4, column = 0, sticky = W, columnspan = 2)

# translation dropdown menu
translation = Checkbutton(mainWindow, text = "translationDropdown")
translation.grid(row = 5, column = 0, sticky = W, columnspan = 2)




# Function to handle the Entry widget focus events
def on_entry_focus_in(event):
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.configure(show="")
        entry.configure(fg="black")

def on_entry_focus_out(event):
    if entry.get() == "":
        entry.delete(0, tk.END)  # Clear the entry if it's empty
        entry.insert(0, placeholder_text)
        entry.configure(show="")
        entry.configure(fg="gray")

        
# Create an Entry widget with placeholder text
placeholder_text = "Enter your input.."
#entry widgets used to take user entry
entry = Entry(mainWindow, fg="gray")
entry.insert(0, placeholder_text)
entry.bind("<FocusIn>", on_entry_focus_in)
entry.bind("<FocusOut>", on_entry_focus_out)

#arranging entry widgets
entry.grid(row=0, column=0, pady=10, padx=20)


# TODO Dynamically update the results variable based on search results, and display it on the right pane
# TODO add a bottom border, and show results based on the checkboxes, and translation dropdown menu

# response on right pane
response = Label(mainWindow, text = results ,padx=5)
response.grid(row=0,column=6, sticky=W, padx=5,pady=2)






# infinite loop which can be terminated by keyboard or mouse interrupt
mainWindow.mainloop()