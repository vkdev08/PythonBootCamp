from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint

import pyperclip
from pyperclip import copy

dict_pwd = {}
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list  = password_letters + password_symbols + password_numbers

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def load_password():
    global dict_pwd
    try:
        with open("password.txt", "r") as file:
            for line in file:
                line = line.strip()
                website, email, password = line.split(" | ")
                if website not in dict_pwd:
                    dict_pwd[website] = {}
                dict_pwd[website][email] = password
    except FileNotFoundError:
        # file doesn't exist yet, first run
        dict_pwd = {}

def save_password():
    global dict_pwd
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # dialogs/Popups - msg box
    all_entered = (len(website) != 0 and len(email) != 0 and len(password) != 0)
    if all_entered:
        is_ok = messagebox.askokcancel(
            title=website,  # ignored on mac
            message=(
                f"Website: {website}\n\n"
                f"📧 Email: {email}\n"
                f"🔑 Password: {password}\n\n"
                f"Do you want to save this?"
            )
        )
        if is_ok:
            if website not in dict_pwd.keys():
                dict_pwd[website] = {}

            dict_pwd[website][email] = password
            with open("password.txt", "w") as file:
                for web in dict_pwd:
                    for email, password in dict_pwd[web].items():
                        file.write(f"{web} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(
            title="Error",
            message="⚠️ Please don't leave any fields empty!\n\n👉 Fill in Website, Email, and Password."
        )

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
load_password()
#image
canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)


#Labels
website_label = Label(window,text=f"Website:")
website_label.grid(row=1,column=0)

email_label = Label(window,text=f"Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(window,text=f"Password:")
password_label.grid(row=3,column=0)

#input
website_entry = Entry(width=36)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"vamsi@gmail.com")
password_entry = Entry(width=20)
password_entry.grid(row=3,column=1)

#buttons
generate_password_button = Button(text="Generate Password",width=11,command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

#dialogs/Popups - msg box
window.mainloop()