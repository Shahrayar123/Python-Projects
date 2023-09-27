from customtkinter import *
from calendar import *


def showCalendar():
    year = int(year_field.get())
    window = CTk()
    window.title(f"{year}")
    window.configure(bg='grey', font=20, padx=100, pady=50)
    window.minsize(width=400, height=400)

    
    output = calendar(year, m=3, l=1, c=8)
    calyear = CTkLabel(window, text=output, font=('monaco', 10, "bold"))
    calyear.grid(row=5, column=1)

    window.mainloop()


root = CTk()
root.title("Calendar")
root.config(background="#222831", padx=100, pady=50)
root.minsize(width=300, height=200)


year_label = CTkLabel(root, text="Enter year", font=('monaco', 30, 'bold'), bg_color="#222831")
year_label.grid(row=0, column=1)

year_field = CTkEntry(root)
year_field.grid(row=3, column=1)

button = CTkButton(root, text="Show Calendar", fg_color="#071952", bg_color="#222831", command=showCalendar)
button.grid(row=4, column=1)

exit_button = CTkButton(root, text="exit", bg_color="#222831", command=exit)
exit_button.grid(row=6, column=1)

root.mainloop()
