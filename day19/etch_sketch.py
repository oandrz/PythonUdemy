from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.back(10)


def rotate_clock_wise():
    turtle.right(10)
    '''
    another approach
    new_heading = heading + 10
    turtle.heading(new_heading)
    '''


def rotate_anti_clock_wise():
    turtle.left(10)


def clear():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=rotate_clock_wise)
screen.onkey(key="a", fun=rotate_anti_clock_wise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
