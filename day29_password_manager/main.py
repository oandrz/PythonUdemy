from tkinter import *
from data_manager import DataManager
from tkinter import messagebox
from password_generator import generate_password
import pyperclip


def handle_search_error(error):
    messagebox.showerror(title=error[0], message=error[1])


def handle_success(credential):
    messagebox.showinfo(
        title="Your password",
        message=f"These are your detail\nemail:{credential['email']}\npassword:{credential['password']}\n"
    )


def search_password():
    key = website_entry.get()
    dm.getPasswordForUrl(key, handle_error=handle_search_error, handle_success=handle_success)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def handle_generate_pass():
    generated_pass = generate_password()
    if len(password_entry.get()) >= 0:
        password_entry.delete(0, END)

    password_entry.insert(index=0, string=generated_pass)
    pyperclip.copy(generated_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
dm = DataManager(path="./cache/data.json")


def handle_validation(field):
    if field == "":
        return False
    else:
        return TRUE


def handleAddButtonClicked():
    url = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    url_validation = handle_validation(url)
    email_validation = handle_validation(url)
    password_validation = handle_validation(url)

    if url_validation and email_validation and password_validation:
        is_okay = messagebox.askokcancel(
            title="Are you sure ?",
            message=f"These are the detail you entered\nemail:{email}\npassword:{password}\n"
                    f"Does the inforamtion correct ?"
        )

        if is_okay:
            dm.savePassword(url, email, password)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Empty Field", message="Please don't leave any fields empty")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./res/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.focus()  # focus to here when apps start
website_entry.grid(row=1, column=1)

search_button = Button(text="Search", width=13, command=search_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, "blaze7906@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
generate_password_button = Button(text="Generate Password", command=handle_generate_pass)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=handleAddButtonClicked)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
