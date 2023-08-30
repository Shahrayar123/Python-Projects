# This uses Tkinter

import os
from tkinter import *
from functools import partial
from tkinter import font, ttk


# Button Colors
cal_button_bg = "#FF6600"
num_button_bg = "#4B4B4B"
other_button_bg = "#DDDDDD"
text_fg = "#FFFFFF"
button_active_bg = "#C0C0C0"
special_color = "#000"
black_fg = "#000"

# root Window
root = Tk()
root.title("Calculator in python")
root.geometry("600x700")
root.resizable(0, 0)

# The buttons Style

num_button = partial(
    Button,
    root,
    fg=text_fg,
    bg=num_button_bg,
    padx=45,
    pady=50,
    activebackground=button_active_bg,
)
calculation_button = partial(
    Button,
    root,
    fg=text_fg,
    bg=cal_button_bg,
    padx=10,
    pady=10,
    activebackground=button_active_bg,
)
s_button = partial(
    Button,
    root,
    fg=text_fg,
    bg=cal_button_bg,
    padx=10,
    pady=10,
    activebackground=button_active_bg,
)

special_button = partial(
    Button,
    root,
    fg=text_fg,
    bg=special_color,
    padx=12.5,
    pady=50,
    activebackground=button_active_bg,
)
clear_button = partial(
    Button,
    root,
    fg=text_fg,
    bg=special_color,
    padx=12.5,
    pady=50,
    activebackground=button_active_bg,
)


# Function /Operations 

# This gets users Input
def get_input(entry, argument):
    entry.insert(END, argument)


# This is for deleting
def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

# clears screen
def clear(entry):
    entry.delete(0, END)

# calculator brain
def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    clear(entry)
    entry.insert(END, output)

# error message
def popupmsg():
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("200x200")
    popup.title("Alert")
    label = Label(popup, text="Cannot divide by 0 ! \n Enter valid values")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    B1.pack()



# This is for the Screen
entry_font = font.Font(size=30)
entry = Entry(root, justify="center", font=entry_font, width=68, border=20)
# entry.grid(row=1, column=12, sticky=N + W + S + E, padx=5, pady=5)
entry.pack(padx=20, pady=90)


# First Row
button9 = num_button(text="9", bg=num_button_bg, command=lambda: get_input(entry, "9"))
button9.place(x=25, y=230)


button8 = num_button(text="8", command=lambda: get_input(entry, "8"))
button8.place(y=230, x=170)


button7 = num_button(text="7", command=lambda: get_input(entry, "7"))
button7.place(y=230, x=315)


backButton = special_button(text="<-", command=lambda: backspace(entry))
backButton.place(x=460, y=230)

clearButton = clear_button(
    text="C/Clear",
    command=lambda: clear(entry),
)
clearButton.place(x=520, y=230)

# second Row
button6 = num_button(text="6", command=lambda: get_input(entry, "6"))
button6.place(y=390, x=25)

button5 = num_button(text="5", command=lambda: get_input(entry, "5"))
button5.place(y=390, x=170)

button4 = num_button(text="4", command=lambda: get_input(entry, "4"))
button4.place(y=390, x=315)

powerButton = Button(root, text='^', fg=text_fg, bg=cal_button_bg, padx=10, pady=10,
                  command=lambda: get_input(entry, '**'))
powerButton.place(y=390, x=460)

divideButton = Button(root, text='/', fg=text_fg, bg=cal_button_bg, padx=10, pady=10,
                  command=lambda: get_input(entry, '/'))
divideButton.place(y=390, x=500)

subtractButton = calculation_button(text='-', command=lambda: get_input(entry, '-'))
subtractButton.place(y=390, x=540)

addButton = Button(root, text='+', fg=text_fg, bg=cal_button_bg, padx=10, pady=3, height=1,width=7,
                  command=lambda: get_input(entry, '+'), activebackground=button_active_bg)

addButton.place(x=475, y=437)


equalButton = Button(root, text='=', fg=text_fg, bg=cal_button_bg, padx=10, pady=10, 
                  command=lambda: calc(entry), activebackground=button_active_bg)
equalButton.place(x=460, y=470)

multiplyButton = calculation_button(text='*', command=lambda: get_input(entry, '*'))
multiplyButton.place(y=470, x=540)

dotButton = s_button(text='.', command=lambda: get_input(entry, '.'))
dotButton.place(y=470, x=500)




# Third Row
button3 = num_button(text="3", command=lambda: get_input(entry, "3"))
button3.place(y=550, x=25)

button2 = num_button(text="2", command=lambda: get_input(entry, "2"))
button2.place(y=550, x=170)

button1 = num_button(text="1", command=lambda: get_input(entry, "2"))
button1.place(y=550, x=315)

button0 = num_button(text="0", command=lambda: get_input(entry, "0"))
button0.place(y=550, x=460)



# def quit():
#     try:
#         exit["command"] = root.quit()
#     except:
#         print("Quited Sucessfully")


# exit = Button(
#     root, text="Quit", fg="white", bg="black", command=quit, height=7, width=7
# )
# exit.place(x=460, y=205)
root.mainloop()
