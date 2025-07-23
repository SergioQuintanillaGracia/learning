from tkinter import *
from tkinter import ttk

root = Tk()
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")
root.title("First GUI")
root.config(padx=20, pady=20)

def calculate():
    res_label.config(text=f"{float(entry.get()) * 1.6}")

# Miles entry
entry = ttk.Entry(takefocus=True, width=8)
entry.grid(row=0, column=1)

# Miles label
miles_label = ttk.Label(text="Miles")
miles_label.grid(row=0, column=2)

# Equal label
equal_label = ttk.Label(text="is equal to")
equal_label.grid(row=1, column=0)

# Result label
res_label = ttk.Label(text="0")
res_label.grid(row=1, column=1)

# Km label
km_label = ttk.Label(text="Km")
km_label.grid(row=1, column=2)

# Calculate button
button = ttk.Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

root.mainloop()