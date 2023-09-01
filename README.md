# SnakeGame

Using OOP and class inheritance as well as the turtle library, I recreated the classic snake game with a few fun modifications. The goal of the game is to collect the circular "food" pieces to add segments to your snake and increase your score. I added a "snake-like" head and made each new piece a random, fun color. Also, every time you gain a new piece the speed of the snake increases (don't worry though, the increase is non-linear so after many pieces it won't get that much faster in order to make the gaming experience more enjoyable). It keeps score at the top, but beware not to run into yourself or the wall.

Update: I changed some things in order to not have a game over but rather to continuously play. I deleted the gameover.py and updated the scoreboard.py (to add highscore attribute and reset method that will keep a high score), and added a reset method to the snake class so that the snake resets after you lose and I reflected all of these changes in the main.py so the game will run these new updates.
Also, I added a highscore.txt and added code into scoreboard.py to save the high score to the txt file so when you play again you can remember your previous score.


![snakegame](https://github.com/andreapeterson/SnakeGame/assets/134665743/17b98e52-27dd-4720-ab7f-a918718de051)
