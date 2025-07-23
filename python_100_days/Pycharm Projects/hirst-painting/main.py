import turtle as t
import random
# import colorgram

# colors = colorgram.extract("mc.jpg", 30)
# rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
#
# print(rgb_colors)

color_list = [(199, 215, 250), (93, 159, 240), (42, 31, 16), (111, 95, 46), (51, 123, 249), (21, 51, 20), (67, 116, 50), (47, 102, 136), (183, 166, 128), (160, 185, 241), (12, 37, 56), (41, 91, 22), (127, 168, 42), (72, 88, 16), (224, 214, 198), (92, 166, 64), (192, 218, 89), (115, 200, 106), (37, 27, 32), (126, 231, 80), (25, 79, 92), (35, 53, 133), (28, 159, 218), (120, 88, 95), (185, 100, 92), (172, 152, 159), (183, 97, 105), (209, 183, 178), (189, 227, 213), (96, 51, 39)]

turt = t.Turtle()
t.colormode(255)
screen = t.Screen()
screen.setup(0.25, 0.5, 500, 200)

turt.speed(100)
turt.penup()
turt.goto(-300, 300)
turt.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

for i in range(10):
    for j in range(10):
        color = random_color()
        turt.color(color)
        turt.fillcolor(color)

        turt.begin_fill()
        turt.circle(10)
        turt.end_fill()

        turt.penup()
        turt.forward(50)
        turt.pendown()

    turt.penup()
    turt.goto(-300, turt.pos()[1] - 50)
    turt.pendown()

screen.exitonclick()