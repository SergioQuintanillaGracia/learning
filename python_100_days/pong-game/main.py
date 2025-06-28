import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

FPS = 165

screen = Screen()
screen.setup(width=800, height=600, startx=900, starty=250)
screen.bgcolor("black")
screen.title("Pong")
# Disable screen auto refreshing
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball(FPS)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    time.sleep(1 / FPS)

    # Detect collisions with walls
    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.bounce_y()

    # Detect collisions with paddles
    if ((ball.xcor() < -330 and ball.distance(l_paddle) < 50) or
            (ball.xcor() > 330 and ball.distance(r_paddle) < 50)):
        ball.bounce_x()
        ball.increase_speed(1.1)

    # Check if the ball was missed by the players
    if ball.xcor() > 390:
        ball.reset_left()
        scoreboard.increase_l(1)
        ball.reset_speed()
    elif ball.xcor() < -390:
        ball.reset_right()
        scoreboard.increase_r(1)
        ball.reset_speed()

screen.exitonclick()