import turtle
from turtle import Turtle, Screen
import random

turt = Turtle()
turtle.colormode(255)
screen = Screen()
screen.setup(0.25, 0.5, 500, 200)

turt.shape("turtle")
turt.color("blue")
turt.speed(100)

# for i in range(4):
#     turt.forward(100)
#     turt.right(90)

# for i in range(50):
#     turt.forward(5)
#     turt.penup()
#     turt.forward(5)
#     turt.pendown()

# for i in range(3, 11):
#     angle = 360 / i
#
#     for j in range(i):
#         turt.forward(80)
#         turt.right(angle)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

# turt.pensize(10)
#
# for i in range(1000):
#     turt.color(random_color())
#     angle = 90 * random.randint(0, 3)
#     turt.right(angle)
#     turt.forward(50)

for i in range(90):
    turt.color(random_color())
    turt.circle(150)
    turt.setheading(turtle.heading() + (i + 1) * 4)

screen.exitonclick()

