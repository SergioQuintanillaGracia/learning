from tkinter import *
from tkinter import ttk

def button_clicked():
    label.config(text=entry.get())

root = Tk()
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")
root.title("First GUI")
root.minsize(width=500, height=300)
root.config(padx=40, pady=40)  # Add space between edges of the window and widgets

# Label
label = Label(text="I am a label", font=("Arial", 24, "bold"))
label.config(text="New text", padx=50, pady=50)
label.grid(column=0, row=0)

# Button
button = ttk.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button2 = ttk.Button(text="Extra")
button2.grid(column=2, row=0)

# Entry
entry = ttk.Entry()
entry.grid(column=4, row=2)

root.mainloop()
