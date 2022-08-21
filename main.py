from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from separator import Separator
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)
ball = Ball()
scoreboard = Scoreboard()
separator = Separator()
separator.dashed_line()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 340 and ball.distance(r_paddle) < 50) or (ball.xcor() < -340 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        ball.refresh()

    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.refresh()

screen.exitonclick()
