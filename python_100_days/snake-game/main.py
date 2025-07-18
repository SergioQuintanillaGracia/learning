from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600, startx=900, starty=250)
screen.bgcolor("black")
screen.title("Snake")
# Disable screen auto refreshing
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score(1)

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()