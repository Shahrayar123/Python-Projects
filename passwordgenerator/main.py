import random
from tkinter import *

letterl = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letteru = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
splchar = "!@#$%^&*"

combine = letterl + letteru + numbers + splchar

pssss = ""

m = Tk(className="password generator")



def cm():
    global pssss
    lee = int(le.get())
    for i in range(lee):
        pssss += random.choice(combine)
    text.set(pssss)
    pssss = " "


m.geometry("400x400")
le = Entry(m)
le.pack()
gen = Button(m, text="generate", width=25, command=cm)
gen.pack()
text = StringVar()
lb = Label(m,textvariable=text)
lb.pack()

m.mainloop()