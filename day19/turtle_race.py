from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def create_turtle(position, x, y):
    turtle = Turtle()
    turtle.color(colors[position])
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(x=x, y=y)
    return turtle

init_x = -230
init_y = 150
for i in range(6):
    turtle = create_turtle(position=i, x=init_x, y=init_y)
    turtles.append(turtle)
    init_y -= 50

is_bet_on = False
if user_bet:
    is_bet_on = True

while is_bet_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_bet_on = False
            if user_bet == turtle.pencolor():
                print(f"You've win! The winning turtle is {turtle.pencolor()}")
            else:
                print(f"You've lost! The winning turtle is {turtle.pencolor()}")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
