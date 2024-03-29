import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    timer_title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    # Wants to convert from min to seconds
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60, "Break", RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60, "Break", PINK)
    else:
        count_down(WORK_MIN * 60, "Work", GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, state, color):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Dynamic Typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    timer_title_label.config(text=state, fg=color)
    if count > 0:
        # just like sleep function but on main thread 2nd param func, 3rd, etc param is the argument that wants to pass
        timer = window.after(1000, count_down, count - 1, state, color)
    elif count == 0:
        start_timer()
        check = ""
        for _ in range(0, math.floor(reps / 2)):
            check += "✓"
        check_label.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_title_label = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW, padx=20)
timer_title_label.grid(row=0, column=1)

# highlightthickness to remove border
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()