from turtle import Turtle


class Car(Turtle):

    def __init__(self, color, pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(color)
        self.goto(pos)
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move_forward(self, speed):
        self.backward(speed)
