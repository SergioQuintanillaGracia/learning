from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)

        # Load highscore
        self.highscore = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())

        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

            # Store new highscore
            with open("data.txt", "w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self, score_amount):
        self.score += score_amount
        self.refresh()