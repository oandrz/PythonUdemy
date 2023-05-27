import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Handle snake when hit food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.plus_score()

    # Handle collision on wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score_board.game_over()

    # Handle tail collision
    for segment in snake.body_segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score_board.game_over()

screen.exitonclick()

