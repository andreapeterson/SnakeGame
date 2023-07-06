from turtle import Turtle
from snake import Snake


class Gameover(Turtle, Snake):
    """Will display Game over in the middle of the screen when called"""

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def end_game(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.write("Game over.", align="center", font=("Courier", 25, "normal"))


