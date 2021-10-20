import pywhatkit
import datetime

num = input("Enter WhatsApp Number of Sender (without Country Code) : ")
msg = input("Enter Your Message : ")
time = input("Enter Time in (HH:MM) 24-hr format : ")
if len(time) != 5:
    print("Invalid. Please make sure HH:MM format is followed, without any extra space (include only 5 characters)")
    exit(1)
h = int(time[0]+time[1])
m = int(time[3]+time[4])
if (h<0 or h>23):
    print("Invalid")
    exit(1)
if (m<0 or m>59):
    print("Invalid")
    exit(1)

pywhatkit.sendwhatmsg(f"+91{num}", f"{msg}", h, m)
