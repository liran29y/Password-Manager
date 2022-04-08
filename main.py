import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# -------------------------------Search ----------------------------------------- #
def search():
    web = web_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showwarning(title="Error",
                               message="No Data File Found")
    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showwarning(title=web,
                                   message=f"email: {email}\npassword:{password}")
        else:
            messagebox.showwarning(title="Error", message=f"No details for {web} exist.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    password = pass_entry.get()
    email = mail_entry.get()
    web = web_entry.get()
    new_data = {web:
                    {"email": email,
                     "password": password}}
    if len(email) == 0 or len(password) == 0 or len(web) == 0:
        messagebox.showwarning(title="empty fields", message="One of your fields are empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, tk.END)
            pass_entry.delete(0, tk.END)
            mail_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels

web_label = tk.Label(text="Website:")
web_label.grid(row=1, column=0)

mail_label = tk.Label(text="Email/Username:")
mail_label.grid(row=2, column=0)

pass_label = tk.Label(text="Password:")
pass_label.grid(row=3, column=0)

# Text Box
web_entry = tk.Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=1)
web_entry.focus()

mail_entry = tk.Entry(width=35)
mail_entry.grid(row=2, column=1, columnspan=1)

pass_entry = tk.Entry(width=30)
pass_entry.grid(row=3, column=1, columnspan=1)

# Buttons
gen_but = tk.Button(text="Generate Password", command=generate_password)
gen_but.grid(row=3, column=2)

search_but = tk.Button(text="Search", command=search)
search_but.grid(row=1, column=2)

add_but = tk.Button(text="Add", width=36, command=save_pass)
add_but.grid(row=4, column=1, columnspan=1)

window.mainloop()
