from turtle import Turtle
import random


class Food(Turtle):
    """Creates the food piece and has a refresh method that spawns it in a random coordinate when called"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_xcor = random.randrange(-280, 280, 20)
        random_ycor = random.randrange(-280, 280, 20)
        self.goto(random_xcor, random_ycor)