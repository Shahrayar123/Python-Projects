import sys
import os
import customtkinter as ctk
import requests as rq
from utils.ipValidator import ipValidate
from utils.timezone_to_time import timeZoneToTime
from tkinter import messagebox

BASE_DIR = os.path.abspath(os.curdir)
ICONBITMAP = os.path.join(BASE_DIR, "assets/imgs/icon.ico/")

sys.path.append(BASE_DIR)

ZeroDivisionError

def ipDefanger(ip: str):
    if ipValidate(ip):
        request = rq.get(f"http://ip-api.com/json/{ip}")
        request = request.json()

        if request['status'] == "success":
            windowIpInfo = ctk.CTkToplevel(window)
            windowIpInfo.title('Ip Defanger Details')
            windowIpInfo.geometry('350x330')
            windowIpInfo.iconbitmap(ICONBITMAP)

            title = ctk.CTkLabel(windowIpInfo, text='Ip Details', font=("Arial", 28, "bold"))
            title.pack(pady=20)

            country = ctk.CTkLabel(windowIpInfo, text=f"Country: {request['country']}", font=("Arial", 15))
            country.pack(anchor="w", padx=20)

            countryCode = ctk.CTkLabel(windowIpInfo, text=f"Country Code: {request['countryCode']}", font=("Arial", 15))
            countryCode.pack(anchor="w", padx=20)

            region = ctk.CTkLabel(windowIpInfo, text=f"region: {request['regionName']}", font=("Arial", 15))
            region.pack(anchor="w", padx=20)

            city = ctk.CTkLabel(windowIpInfo, text=f"City: {request['city']}", font=("Arial", 15))
            city.pack(anchor="w", padx=20)

            lat = ctk.CTkLabel(windowIpInfo, text=f"Lat: {request['lat']}", font=("Arial", 15))
            lat.pack(anchor="w", padx=20)

            lon = ctk.CTkLabel(windowIpInfo, text=f"City: {request['lon']}", font=("Arial", 15))
            lon.pack(anchor="w", padx=20)

            timezone = ctk.CTkLabel(windowIpInfo, text=f"Timezone: {request['timezone']}", font=("Arial", 15))
            timezone.pack(anchor="w", padx=20)

            time = ctk.CTkLabel(windowIpInfo, text=f"Time: {timeZoneToTime(request['timezone'])}", font=("Arial", 15))
            time.pack(anchor="w", padx=20)

            window.mainloop()
        else:
            messagebox.showerror(title='Ip Defanger Error', message=request['message'])
    else:
        messagebox.showerror(title='Ip Defanger Error', message="This address is not a valid IP")


window = ctk.CTk()
window.title("Ip Defanger")
window.geometry("400x100")
window.iconbitmap(ICONBITMAP)

ip_entry = ctk.StringVar()
ip_entry = ctk.CTkEntry(window, placeholder_text="Write the ip here", width=300)
ip_entry.pack(pady=10)

button = ctk.CTkButton(
    window,
    width=300,
    height=30,
    text="Track IP",
    command=lambda: ipDefanger(ip=ip_entry.get()),
)
button.pack(pady=1)

window.mainloop()
