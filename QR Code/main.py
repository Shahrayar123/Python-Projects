# Importing the modules
from tkinter import *
import time
import pyqrcode
import os  # For checking and creating directories

# QR Code generation function
def gen_qr():
    global qr, img
    qr = pyqrcode.create(con.get())
    qr_xbm = qr.xbm(scale=5)
    img = BitmapImage(data=qr_xbm, foreground='black', background='white')
    l4.config(image=img)
    l4.image = img  # To prevent garbage collection

# Save the QR code as a PNG file in 'static' folder
def save():
    # Generate the QR code
    gen_qr()
    
    # Create 'static' folder if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')
    
    # Get the current time as a unique filename
    tme = time.time()
    
    # Save the QR code in the 'static' folder with a unique name
    qr.png(f'static/{tme}.png', scale=8)
    
    # Clear the input field after saving
    con.set('')

# Main window setup
wind = Tk()
wind.title('QR Code Generator')	
wind.geometry('400x500')
wind.resizable(0, 0)
wind.config(bg="#f4f4f9")

# Variable for QR code content
con = StringVar()


f1 = Frame(wind, bg='#2c3e50', pady=20)
f1.pack(fill="x")
f2 = Frame(wind, bg='#ecf0f1', pady=20)
f2.pack(fill="x")
f3 = Frame(wind, bg='#ecf0f1', pady=20)
f3.pack(fill="x")


l1 = Label(f1, text='QR Code Generator', font=('Arial', 20, 'bold'), fg='white', bg='#2c3e50')
l1.pack(pady=5)


l2 = Label(f1, text='By Harshit', font=('Arial Rounded MT Bold', 12), fg='#bdc3c7', bg='#2c3e50')
l2.pack(pady=5)


l3 = Label(f2, font=('Arial', 12), text='Enter the content:', fg='#34495e', bg='#ecf0f1')
l3.grid(row=0, column=0, padx=10, pady=10)


e1 = Entry(f2, textvariable=con, width=30, font=('Arial', 12), fg='#2c3e50', bg='#ffffff', borderwidth=2, relief="groove")
e1.grid(row=0, column=1, padx=10, pady=10)


b1 = Button(f2, text='Generate', command=gen_qr, font=('Arial', 12, 'bold'), bg='#27ae60', fg='white', relief=FLAT, padx=10, pady=5)
b1.grid(row=1, column=0, padx=10, pady=20)

b2 = Button(f2, text='Save', command=save, font=('Arial', 12, 'bold'), bg='#2980b9', fg='white', relief=FLAT, padx=10, pady=5)
b2.grid(row=1, column=1, padx=10, pady=20)

l4 = Label(f3, text="QR Code Preview", bg='#ffffff', relief='sunken', width=200, height=200)
l4.pack(padx=20, pady=20)

wind.mainloop()
