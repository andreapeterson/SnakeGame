import turtle as t
import random

X_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray", "white"]


class Snake:
    """Makes the snake and moves it and adds segments"""

    def __init__(self):
        self.segments = []
        self.original_snake()
        self.head_mod()

    def original_snake(self):
        for snake_piece in range(0, 3):
            snake = t.Turtle(shape="square")
            snake.color(random.choice(colors))
            snake.penup()
            snake.shapesize(0.9, 0.9)
            snake.goto(x=X_POSITIONS[snake_piece], y=0)
            self.segments.append(snake)

    def head_mod(self):
        self.segments[0].shape("circle")
        self.segments[0].shapesize(0.8, 1)

    def extend_snake(self):
        snake = t.Turtle(shape="square")
        snake.color(random.choice(colors))
        snake.penup()
        snake.goto(1000, 1000)
        snake.shapesize(0.9, 0.9)
        self.segments.append(snake)
        snake.goto(self.segments[-1].position())
        snake.color(random.choice(colors))

    def move_snake(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            x_goto = self.segments[segment_num - 1].xcor()
            y_goto = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(x=x_goto, y=y_goto)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def reset(self):
        for segment in self.segments:
            segment.reset()
        self.segments.clear()
        self.__init__()



