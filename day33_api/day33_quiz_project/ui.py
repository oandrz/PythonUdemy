from tkinter import *
from quiz_brain import QuizBrain


FONT_BODY = ("Ariel", 20, "italic")
THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
BLACK = "#000000"
GREEN = "#00FF00"
RED = "#FF0000"


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzle")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = self._create_score_text()
        self.quiz_canvas = self._create_quiz_card()
        self.true_button = self._create_true_button()
        self.false_button = self._create_false_button()

        self.get_next_question()
        self.window.mainloop()

    def _create_score_text(self):
        score_text = Label(text=f"Score:{self.quiz_brain.score}", bg=THEME_COLOR, fg=WHITE, highlightthickness=0, anchor="center")
        score_text.grid(row=0, column=1)

        return score_text

    def _create_quiz_card(self):
        canvas = Canvas(width=300, height=250, bg=WHITE, highlightthickness=0)
        self.quiz_text = canvas.create_text(
            150,
            125,
            text="Give your quiz text here",
            fill=BLACK,
            font=FONT_BODY,
            width=280
        )
        canvas.grid(row=1, column=0, columnspan=2, pady=50)

        return canvas

    def _create_true_button(self):
        self.true_image = PhotoImage(file="./images/true.png")
        button = Button(
            image=self.true_image,
            highlightbackground=THEME_COLOR,
            highlightthickness=0,
            command=self.handle_true
        )
        button.grid(row=2, column=0)

        return button

    def _create_false_button(self):
        self.false_image = PhotoImage(file="./images/false.png")
        image_button = Button(
            image=self.false_image,
            highlightbackground=THEME_COLOR,
            highlightthickness=0,
            command=self.handle_false
        )
        image_button.grid(row=2, column=1)

        return image_button

    def get_next_question(self):
        self.quiz_canvas.config(bg=WHITE)
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            question = self.quiz_brain.next_question()
            self.quiz_canvas.itemconfig(self.quiz_text, text=question)
        else:
            self.quiz_canvas.itemconfig(self.quiz_text, text="The End.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def handle_true(self):
        self.give_feedback(self.quiz_brain.check_answer(user_answer="True"))

    def handle_false(self):
        self.give_feedback(self.quiz_brain.check_answer(user_answer="False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.quiz_canvas.config(bg=GREEN)
        else:
            self.quiz_canvas.config(bg=RED)

        self.window.after(1000, self.get_next_question)
