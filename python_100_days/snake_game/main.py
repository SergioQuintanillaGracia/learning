from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600, startx=900, starty=250)
screen.bgcolor("black")
screen.title("Snake")
# Disable screen auto refreshing
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    snake.move()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()