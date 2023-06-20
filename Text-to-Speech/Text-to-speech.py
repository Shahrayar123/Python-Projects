import tkinter as tk
from tkinter import * 
import pyttsx3

engine = pyttsx3.init(driverName='espeak')


def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

root=Tk()

textv=StringVar()

obj=LabelFrame(root,text="Text to speech",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lb1=Label(obj,text="Text",font=30)
lb1.pack(side=tk.LEFT,padx=5)

text=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="Speak",font=20,bg="green",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)

root.title("Text to speech")
root.geometry("480x200")
root.resizable(False,False)
root.mainloop()