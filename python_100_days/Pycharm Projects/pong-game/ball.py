from turtle import Turtle

class Ball(Turtle):
    def __init__(self, fps):
        super().__init__()
        self.fps = fps
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_pos()

        self.dir_x = 1
        self.dir_y = 1
        self.speed = 1

    def move(self):
        new_x = self.xcor() + 240 * self.dir_x * self.speed / self.fps
        new_y = self.ycor() + 180 * self.dir_y * self.speed / self.fps
        self.goto(new_x, new_y)

    def increase_speed(self, mult):
        self.speed *= mult

    def reset_speed(self):
        self.speed = 1

    def reset_left(self):
        self.dir_x = -1
        self.dir_y = 1
        self.reset_pos()

    def reset_right(self):
        self.dir_x = 1
        self.dir_y = 1
        self.reset_pos()

    def reset_pos(self):
        self.goto(0, 0)

    def bounce_x(self):
        self.dir_x *= -1

    def bounce_y(self):
        self.dir_y *= -1