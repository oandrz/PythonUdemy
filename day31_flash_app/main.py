import random
from tkinter import *
from data_manager import DataManager

BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#000000"
WHITE = "#FFFFFF"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_BODY = ("Ariel", 60, "bold")
FRENCH_KEY = "French"
ENGLISH_KEY = "English"
focused_index = None

data_manager = DataManager("./data/french_words.csv")
words = data_manager.get_words()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def right_answer():
    if focused_index is not None:
        words.remove(words[focused_index])
        data_manager.save_remaining_words(words)
    start_timer()


def start_timer():
    global focused_index
    focused_index = random.randint(0, len(words))

    generate_french()
    window.after(3000, generate_english)


def generate_french():
    canvas.itemconfig(card_image, image=front_img)
    canvas.itemconfig(text, text=words[focused_index][FRENCH_KEY], fill=BLACK)
    canvas.itemconfig(title, text=FRENCH_KEY, fill=BLACK)


def generate_english():
    canvas.itemconfig(card_image, image=background_img)
    canvas.itemconfig(text, text=words[focused_index][ENGLISH_KEY], fill=WHITE)
    canvas.itemconfig(title, text=ENGLISH_KEY, fill=WHITE)


canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
background_img = PhotoImage(file="./images/card_back.png")
front_img = PhotoImage(file="./images/card_front.png")
card_image = canvas.create_image(400, 263, image=front_img)

title = canvas.create_text(400, 150, text="", fill=BLACK, font=FONT_TITLE)
text = canvas.create_text(400, 263, text="", fill=BLACK, font=FONT_BODY)

canvas.grid(row=0, column=0, columnspan=2)

reject_img = PhotoImage(file="./images/wrong.png")
reject_button = Button(
    text="reject",
    image=reject_img,
    highlightbackground=BACKGROUND_COLOR,
    highlightthickness=0,
    command=start_timer
)
reject_button.grid(row=1, column=0)

accept_image = PhotoImage(file="./images/right.png")
accept_button = Button(
    text="approve",
    image=accept_image,
    highlightbackground=BACKGROUND_COLOR,
    highlightthickness=0,
    command=right_answer
)
accept_button.grid(row=1, column=1)

start_timer()

window.mainloop()
