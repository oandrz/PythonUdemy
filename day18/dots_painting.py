# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('./res/hrist.jpg', 6)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
import turtle as t
import random
from turtle import Turtle, Screen

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57)]
t.colormode(255)

turtle = Turtle()
turtle.hideturtle()


def draw_spot_painting(size, dots_size):
    turtle.penup()
    for row in range(size):
        if row % 2 == 0 or row == 0:
            turtle.setheading(180)
        else:
            turtle.setheading(0)

        for col in range(size):
            turtle.dot(dots_size, random.choice(color_list))

            if col < size - 1:
                turtle.forward(dots_size * 2)

        turtle.setheading(90)
        turtle.forward(dots_size * 2)


draw_spot_painting(10, 20)

screen = Screen()
screen.exitonclick()
