from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "bold"))

    def increase_l(self, amount):
        self.l_score += 1
        self.update()

    def increase_r(self, amount):
        self.r_score += 1
        self.update()