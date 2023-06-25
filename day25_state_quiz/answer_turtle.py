from turtle import Turtle


class AnswerTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def showAnswer(self, state):
        cor_x = int(state.x.item())
        cor_y = int(state.y.item())
        state = state.state.item()
        self.goto(cor_x, cor_y)
        self.write(state)
