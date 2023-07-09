import turtle as t
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

# Screen set-up
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
score.keep_score()


screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)


game_on = True
while game_on:
    screen.update()

    # Speed will get faster but in a non-linear fashion
    time.sleep(10 / int(score.score + 100))
    snake.move_snake()

    # if the snake head is closest enough to the food, it will add a segment to the snake and increase the score and
    # reset the food
    if snake.segments[0].distance(food) < 15:
        screen.tracer(0)
        snake.extend_snake()
        score.increase_score()
        food.refresh()

    # To trigger game over if snake runs into wall
    if abs(snake.segments[0].xcor()) > 285 or abs(snake.segments[0].ycor()) > 285:
        score.reset()
        snake.reset()

    # To trigger game over if snake runs into itself
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
