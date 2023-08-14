import random
import tkinter as tk
from tkinter import ttk
import time


"""
 Funtion start() create the magic number, number of attemps, and ask user for input
"""
def start():
    global magic_number
    magic_number = random.randint(1, 100)
    print(magic_number)
        
mainWindow = tk.Tk()
global attempts
attempts = 0

titleLabel = ttk.Label(master=mainWindow, text = 'Number Guessing Game', font=('Helvetica', 50, 'bold'))

global guessLabel
guessLabel = ttk.Label(master=mainWindow, text = 'Guess a Number Between one and 100', font=('Helvetica', 230))


mainWindow.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
mainWindow.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

titleLabel.grid(row=0, sticky='N', pady=(20, 0), padx=40)

corrLabel = ttk.Label(master=mainWindow, text='Guess a number between 1 and 100', font=('Helvetica', 20, 'italic'))


entryVar = tk.StringVar()

start()

def check_win():
    global attempts
    attempts += 1
    player_guess = entryVar.get()
    try:
        player_guess = int(player_guess)
    except:
        corrLabel.config(text='Invalid Input', foreground='red')
        resetGuess()
    
    if player_guess > magic_number:
        corrLabel.config(text='Too Big', foreground='red')
        resetGuess()
    elif player_guess < magic_number:
        corrLabel.config(text='Too Small', foreground='red')
        resetGuess()
    elif player_guess == magic_number:
        corrLabel.config(text='Correct, it took you ' + str(attempts) + " attempts.", foreground='green')
        mainWindow.update()
        time.sleep(1)
        corrLabel.config(text='Restarting Game', foreground='blue')
        mainWindow.update()
        resetGuess()
        start()
    
def resetGuess():
    mainWindow.update()
    time.sleep(1)
    corrLabel.config(text='Guess a number between 1 and 100', foreground='white')
  
entry = ttk.Entry(master=mainWindow, textvariable=entryVar)
entryButton = ttk.Button(master=mainWindow, text='Submit', command=check_win)    
entry.grid(row=1, sticky='N', padx=(0, 110), pady=(30, 0))
entryButton.grid(row=1, padx=(0, 180), sticky='EN', pady=(30, 0))

corrLabel.grid(sticky='N', pady=40)
mainWindow.mainloop()
