def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f + 459.67) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k * 9/5) - 459.67

def convert_temperature():
    temp = float(entry_temp.get())
    unit = var_unit.get()

    if unit == 'Celsius':
        f = celsius_to_fahrenheit(temp)
        k = celsius_to_kelvin(temp)
        result_f.config(text=f"Fahrenheit: {f:.2f}")
        result_k.config(text=f"Kelvin: {k:.2f}")
    elif unit == 'Fahrenheit':
        c = fahrenheit_to_celsius(temp)
        k = fahrenheit_to_kelvin(temp)
        result_c.config(text=f"Celsius: {c:.2f}")
        result_k.config(text=f"Kelvin: {k:.2f}")
    elif unit == 'Kelvin':
        c = kelvin_to_celsius(temp)
        f = kelvin_to_fahrenheit(temp)
        result_c.config(text=f"Celsius: {c:.2f}")
        result_f.config(text=f"Fahrenheit: {f:.2f}")
import tkinter as tk

root = tk.Tk()
root.title("Temperature Conversion")

tk.Label(root, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=10)
entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Select Unit:").grid(row=1, column=0, padx=10, pady=10)
var_unit = tk.StringVar(value="Celsius")
tk.Radiobutton(root, text="Celsius", variable=var_unit, value="Celsius").grid(row=1, column=1)
tk.Radiobutton(root, text="Fahrenheit", variable=var_unit, value="Fahrenheit").grid(row=1, column=2)
tk.Radiobutton(root, text="Kelvin", variable=var_unit, value="Kelvin").grid(row=1, column=3)

tk.Button(root, text="Convert", command=convert_temperature).grid(row=2, column=1, pady=10)

result_c = tk.Label(root, text="Celsius: ")
result_c.grid(row=3, column=0, columnspan=4)
result_f = tk.Label(root, text="Fahrenheit: ")
result_f.grid(row=4, column=0, columnspan=4)
result_k = tk.Label(root, text="Kelvin: ")
result_k.grid(row=5, column=0, columnspan=4)

root.mainloop()
