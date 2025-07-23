import json
import pyperclip
from random import choice, shuffle, randint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)

    return password

def create_random_password():
    password = get_random_password()
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Fill every field", message="Please, fill every field!")
        return

    try:
        with open("data.json", "r") as f:
            # Load and update data
            data = json.load(f)
            data.update(new_data)

        with open("data.json", "w") as f:
            # Dump updated data to file
            json.dump(data, f, indent=4)

    except FileNotFoundError:
        with open("data.json", "w") as f:
            json.dump(new_data, f, indent=4)

    entry_website.delete(0, END)
    entry_password.delete(0, END)

# ----------------------- SEARCHING PASSWORDS -------------------------- #
def search():
    website = entry_website.get().strip()

    if len(website) == 0:
        messagebox.showinfo(title="Empty website", message="The website field is empty, enter a website")
        return

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            email = data[website]["email"]
            password = data[website]["password"]

    except (FileNotFoundError, KeyError):
        messagebox.showinfo(title="Error", message=f"There are no credentials stored for website \"{website}\"")

    else:
        messagebox.showinfo(title=f"{website} credentials", message=f"Website: {website}\nEmail: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")
root.title("MyPass")
root.config(padx=40, pady=40)

# Logo
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# Website
label_website = Label(text="Website: ")
label_website.grid(row=1, column=0)
entry_website = ttk.Entry(width=22)
entry_website.focus()
entry_website.grid(row=1, column=1, pady=4)
button_search = ttk.Button(text="Search", command=search, width=10)
button_search.grid(row=1, column=2)

# Email / Username
label_email = Label(text="Email / Username: ")
label_email.grid(row=2, column=0)
entry_email = ttk.Entry(width=35)
entry_email.insert(0, "example@gmail.com")
entry_email.grid(row=2, column=1, columnspan=2, pady=4)

# Password
label_password = Label(text="Password: ")
label_password.grid(row=3, column=0)
entry_password = ttk.Entry(width=22)
entry_password.grid(row=3, column=1, pady=4)
button_password = ttk.Button(text="Generate", command=create_random_password, width=10)
button_password.grid(row=3, column=2)

# Add button
button_add = ttk.Button(text="Add", command=save, width=34)
button_add.grid(row=4, column=1, columnspan=2, pady=4, padx=4)

root.mainloop()