from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0

        self.update()

    def update(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self, amount):
        self.score += amount
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)