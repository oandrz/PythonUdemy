from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_value_label = Label(text="0")
km_value_label.grid(row=1, column=1)

km_unit_label = Label(text="Km")
km_unit_label.grid(row=1, column=2)


def handle_calculate_click():
    miles = float(miles_input.get())
    miles_in_km = miles * 1.6
    km_value_label["text"] = str(round(miles_in_km))


calculate_button = Button(text="Calculate", command=handle_calculate_click)
calculate_button.grid(row=2, column=1)

window.mainloop()
