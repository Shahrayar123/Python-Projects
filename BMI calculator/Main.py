from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#1e1e1e")  # Sfondo scuro

def BMI():
    h = float(Height.get())
    w = float(Weight.get())

    m = h / 100
    bmi = round(float(w / m**2), 1)
    label1.config(text=bmi)

    if bmi <= 18.5:
        label2.config(text="Underweight!")
        label3.config(text="Lower weight than normal body!")
    elif 18.5 < bmi <= 25:
        label2.config(text="Normal!")
        label3.config(text="You are healthy!")
    elif 25 < bmi < 30:
        label2.config(text="Overweight!")
        label3.config(text="You are slightly overweight!")
    else:
        label2.config(text="Obese!")
        label3.config(text="Health may be at risk!")

# Icon
image_icon = PhotoImage(file="Sprites/bmiIcon.png")
root.iconphoto(False, image_icon)


# Mostra l'immagine in un'etichetta

top = PhotoImage(file="Sprites/Sif247.png")
top_image = Label(root, image = top, background="#f0f1f5")
top_image.place(x = -10, y=-10)

# Bottom box
Label(root, width=72, height=18, bg="#2a2a2a").pack(side=BOTTOM)

# Two boxes
box = PhotoImage(file="Sprites/box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

# Scale
scale = PhotoImage(file="Sprites/scale.png")
Label(root, image=scale, bg="#2a2a2a").place(x=20, y=310)

# Slider1
current_value = tk.DoubleVar()

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    size = int(float(get_current_value()))
    img = Image.open("Sprites/Man.png")
    resized_image = img.resize((150, 30 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=525 - size)
    secondimage.image = photo2

style = ttk.Style()
style.configure("TScale", background="white")

slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale",
                   command=slider_changed, variable=current_value)
slider.place(x=80, y=250)

# Slider2
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{:.2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

style2 = ttk.Style()
style2.configure("TScale", background="white")

slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale",
                     command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

# Entry box
Height = StringVar()
Weight = StringVar()

Label(root, text="Height: cm", font='arial 12', bg='#1e1e1e', fg='#fff').place(x=35, y=130)
Label(root, text="Weight: kg", font='arial 12', bg='#1e1e1e', fg='#fff').place(x=255, y=130)


height = Entry(root, textvariable=Height, width=5, font='arial 50', bg='#444', fg='#fff', bd=0, justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg='#444', fg='#fff', bd=0, justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())

# Man image
secondimage = Label(root, bg="#2a2a2a")
secondimage.place(x=70, y=530)

Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#3b5998", fg="white", command=BMI).place(x=280, y=340)

label1 = Label(root, font="arial 60 bold", bg="#2a2a2a", fg="#fff")
label1.place(x=250, y=400)

label2 = Label(root, font="arial 20 bold", bg="#2a2a2a", fg="#fff")
label2.place(x=250, y=480)

label3 = Label(root, font="arial 10 bold", bg="#2a2a2a", fg="#fff")
label3.place(x=250, y=550)

root.mainloop()
