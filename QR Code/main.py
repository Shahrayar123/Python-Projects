'''Python Program - QR Code generating by DJ Harshit'''

# Importing the modules
from tkinter import *
import time
import pyqrcode

def gen_qr():
    global qr, img
    qr = pyqrcode.QRCode(con.get())
    qr_xbm = qr.xbm(scale=5)
    img = BitmapImage(data=qr_xbm, foreground='black', background='white')
    l4.config(image=img)

def save():
    gen_qr()
    tme = time.time()
    qr.png(f'{tme}.png', scale=8)
    con.set('')

# Main program
wind = Tk()
wind.title('QR Code Gen')	
wind.geometry('500x400')
wind.resizable(0,0)

# Variable
con = StringVar()

f1 = Frame(wind, width=500, height=100)
f1.pack()
f2 = Frame(wind, width=500, height=50)
f2.pack()
f3 = Frame(wind, width=500, height=250)
f3.pack()

l1 = Label(f1, text='QR Code Generator', font=('SugarFont Bold', 30, 'bold'))
l1.grid(row=0, column=0, columnspan=3, padx=5, pady=10)
l2 = Label(f1, text='By Harshit', font=('Arial Rounded MT Bold', 15))
l2.grid(row=0, column=4, sticky='w', pady=10)

l3 = Label(f2, font=('', 10), text='Enter the content')
l3.grid(row=0, column=0, padx=5)

e1 = Entry(f2, textvariable=con, width=40)
e1.grid(row=0, column=1, padx=5)

b1 = Button(f2, text='Generate', command=gen_qr)
b1.grid(row=1, column=0, pady=10)

b2 = Button(f2, text='Save', command=save)
b2.grid(row=1, column=1, pady=10)

l4 = Label(f3, pady=5)
l4.pack()

wind.mainloop()