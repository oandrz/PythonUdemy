import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
turtle = Player()
manager = CarManager()
screen.onkey(fun=turtle.move_forward, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    manager.generate_car()
    manager.move_cars()

    if manager.detect_collision(turtle):
        scoreboard.game_over()
        game_is_on = False

    if turtle.ycor() >= 280:
        scoreboard.level_up()
        manager.add_speed()
        turtle.reset_player()

    screen.update()

screen.exitonclick()
