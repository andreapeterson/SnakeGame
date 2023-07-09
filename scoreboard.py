from turtle import Turtle


class Scoreboard(Turtle):
    """Keeps score at the top of the screen and can increase it"""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            contents = file.read()
            self.high_score = int(contents)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def keep_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", align="center", font=("Courier", 25, "normal"))

    def increase_score(self):
        self.score += 1
        self.keep_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.keep_score()
