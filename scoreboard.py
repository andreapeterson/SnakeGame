from turtle import Turtle


class Scoreboard(Turtle):
    """Keeps score at the top of the screen and can increase it"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()

    def keep_score(self):
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score}", align="center", font=("Courier", 25, "normal"))

    def increase_score(self):
        self.score += 1
        self.write(f"Score:{self.score}", align="center", font=("Courier", 25, "normal"))


