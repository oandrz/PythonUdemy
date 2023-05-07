from turtle import Turtle, Screen
import turtle as t
import random

'''
Example of creating square shape
'''
# timmy_turtle = Turtle()
# timmy_turtle.shape("turtle")
# timmy_turtle.color("green")
# timmy_turtle.dot(20, "red")
# for _ in range(4):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(90)

'''
Example of creating dash line
'''
# turtle = Turtle()
# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

'''
Example of creating triangle, square, pentagon, hexagon, heptagon, octagon, nanogon, decagon
'''
# turtle = Turtle()
#
# colors = ["red", "blue", "green", "orange", "purple", "black", "teal", "pink"]
#
#
# def draw_shape(turtle_locale, side, length, color):
#     for _ in range(side):
#         turtle_locale.color(color)
#         turtle_locale.forward(length)
#         turtle_locale.right(360 / side)
#
#
# for n_shape in range(3, 11):
#     draw_shape(turtle_locale=turtle, side=n_shape, length=100, color=colors[n_shape - 3])

'''
Example of random walk
'''


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


#
# directions = [0, 90, 180, 270]
t.colormode(255)
# turtle = Turtle()
#
# turtle.shape("turtle")
# turtle.speed(10)
# turtle.pensize(width=20)
#
# for _ in range(1000):
#     turtle.color(random_color())
#     turtle.forward(50)
#     turtle.setheading(random.choice(directions))


'''
Example of spirograph
'''
turtle = Turtle()
turtle.speed("fastest")


def draw_spirograph(size):
    for i in range(int(360 / size)):
        turtle.color(random_color())
        turtle.circle(radius=100)
        current_heading = turtle.heading()
        turtle.setheading(current_heading + size)


draw_spirograph(size=5)

screen = Screen()
screen.exitonclick()
