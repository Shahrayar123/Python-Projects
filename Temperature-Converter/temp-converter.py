import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    temperature = entry.get()
    try:
        temperature = float(temperature)
        selected_unit = unit_choices.get()
        
        if selected_unit == "Celsius":
            if selected_choice.get() == "Kelvin":
                converted_temp = temperature + 273.15
                messagebox.showinfo("Conversion Result", f"{temperature}°C is equivalent to {converted_temp} K")
            elif selected_choice.get() == "Fahrenheit":
                converted_temp = (temperature * 9/5) + 32
                messagebox.showinfo("Conversion Result", f"{temperature}°C is equivalent to {converted_temp}°F")
                
        elif selected_unit == "Kelvin":
            if selected_choice.get() == "Celsius":
                converted_temp = temperature - 273.15
                messagebox.showinfo("Conversion Result", f"{temperature} K is equivalent to {converted_temp}°C")
            elif selected_choice.get() == "Fahrenheit":
                converted_temp = (temperature - 273.15) * 9/5 + 32
                messagebox.showinfo("Conversion Result", f"{temperature} K is equivalent to {converted_temp}°F")
                
        elif selected_unit == "Fahrenheit":
            if selected_choice.get() == "Celsius":
                converted_temp = (temperature - 32) * 5/9
                messagebox.showinfo("Conversion Result", f"{temperature}°F is equivalent to {converted_temp}°C")
            elif selected_choice.get() == "Kelvin":
                converted_temp = (temperature - 32) * 5/9 + 273.15
                messagebox.showinfo("Conversion Result", f"{temperature}°F is equivalent to {converted_temp} K")
                
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid temperature value.")

# Create the tkinter window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("300x200")  # Set the initial window size

# Create the entry field
entry = tk.Entry(window)
entry.pack()

# Create the dropdown menu for temperature unit choices
unit_choices = tk.StringVar(window)
unit_choices.set("Celsius")  # Set the default unit as Celsius
unit_dropdown = tk.OptionMenu(window, unit_choices, "Celsius", "Kelvin", "Fahrenheit")
unit_dropdown.pack()

# Create the radio buttons for temperature choices
selected_choice = tk.StringVar(window, "Celsius")  # Set the default choice as Celsius

kelvin_radio = tk.Radiobutton(window, text="Kelvin", variable=selected_choice, value="Kelvin")
kelvin_radio.pack()

celsius_radio = tk.Radiobutton(window, text="Celsius", variable=selected_choice, value="Celsius")
celsius_radio.pack()

fahrenheit_radio = tk.Radiobutton(window, text="Fahrenheit", variable=selected_choice, value="Fahrenheit")
fahrenheit_radio.pack()

# Create the conversion button
convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack()

# Run the tkinter event loop
window.mainloop()
