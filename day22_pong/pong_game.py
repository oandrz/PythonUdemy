import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

"""
pong game:
- ball class
- paddle class
- score board class
- screen class
"""
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

score_board = ScoreBoard()
ball = Ball()
right_paddle = Paddle(start_pos_x=350, start_pos_y=0)
left_paddle = Paddle(start_pos_x=-350, start_pos_y=0)
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380:
        ball.reset()
        score_board.right_point()

    if ball.xcor() < -380:
        ball.reset()
        score_board.left_point()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()








screen.exitonclick()
