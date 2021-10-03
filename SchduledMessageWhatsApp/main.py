import pywhatkit
import datetime

num = input("Enter sender's Whatsapp number without your country code : ")
link = input("Enter Your Message : ")
time = input("Enter Time in (HH:MM) 24-hr format : ")
if len(time) != 5:
    print("Invalid Input!!")
    exit()
h = int(time[0]+time[1])
m = int(time[3]+time[4])
if (h<0 or h>23):
    print("Invalid Input!!")
    exit()
if (m<0 or m>59):
    print("Invalid Input!!")
    exit()

pywhatkit.sendwhatmsg(f"+91{num}", f"{link}", h, m)
