import tkinter as tk
from tkinter import messagebox
from math import radians, sin, cos, sqrt, atan2


# Haversine formula to calculate distance
def calculate_distance():
    try:
        lat1, lon1 = map(float, [entry_lat1.get(), entry_lon1.get()])
        lat2, lon2 = map(float, [entry_lat2.get(), entry_lon2.get()])

        R = 6371  # Radius of Earth in km
        dlat = radians(lat2 - lat1)
        dlon = radians(lat2 - lon1)
        a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(
            dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        result_label.config(text=f"Distance: {distance:.2f} km", fg='#00FF00')
    except ValueError:
        messagebox.showerror("Input Error",
                             "Please enter valid numbers for coordinates!")


# Creating the main window
root = tk.Tk()
root.title("Distance Calculator")
root.geometry("400x500")
root.configure(bg="#2C3E50")
root.resizable(False, False)




# Title Label
title_label = tk.Label(root,
                       text="Distance Calculator",
                       font=("Arial", 16, "bold"),
                       fg="#FFFFFF",
                       bg="#2C3E50")
title_label.pack(pady=10)


# Input Fields
def create_label_entry(text, y_pos):
    label = tk.Label(root,
                     text=text,
                     font=("Arial", 12),
                     fg="#ECF0F1",
                     bg="#2C3E50")
    label.place(x=50, y=y_pos)
    entry = tk.Entry(root,
                     font=("Arial", 12),
                     width=20,
                     bg="#34495E",
                     fg="#FFFFFF",
                     relief="flat",
                     justify="center")
    entry.place(x=180, y=y_pos)
    return entry


entry_lat1 = create_label_entry("Latitude 1:", 70)
entry_lon1 = create_label_entry("Longitude 1:", 110)
entry_lat2 = create_label_entry("Latitude 2:", 150)
entry_lon2 = create_label_entry("Longitude 2:", 190)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Distance", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", relief="flat", padx=10, pady=5, command=calculate_distance)
calculate_button.place(x=120, y=230)


# Result Label

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#00FF00", bg="#2C3E50")
result_label.place(x=50, y=280)


# Run the app
root.mainloop()
