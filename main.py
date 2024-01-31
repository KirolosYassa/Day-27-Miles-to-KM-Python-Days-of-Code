from tkinter import *


def calculate_miles_to_km():
    miles_value = input_miles.get()
    km_converted_value = round(float(miles_value) * 1.6)
    km_converter_value_label.config(text=str(km_converted_value))



Window = Tk()
Window.title("Miles to KM Converter") 
Window.config(padx=10, pady=10)
Window.minsize(width=250, height=100)

input_miles = Entry()
input_miles.config(width=10)
input_miles.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_converter_value_label = Label(text="0")
km_converter_value_label.grid(column=1, row=1)

KM_label = Label(text="KM")
KM_label.grid(column=2, row=1)

btn = Button(text="Calculate", command=calculate_miles_to_km)
btn.grid(column=1, row=2)



Window.mainloop()