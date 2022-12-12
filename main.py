from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("DJ Snake!")
screen.tracer(0)

# Initialize objects
score = 0
tim = Snake()
food = Food()
board = Scoreboard()

# Define screen events
screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.left, "Left")
screen.onkey(tim.right, "Right")

# Start the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    tim.move_snake()

    # Detect collision with food
    if tim.head.distance(food) < 15:
        board.update_score()
        board.write_score()
        tim.add_segment()
        food.move()

    # Detect collision with wall
    if tim.head.xcor() > 280 or tim.head.xcor() < -290 or tim.head.ycor() > 290 or tim.head.ycor() < -290:
        board.update_high_score()
        tim.reset_snake()

    # Detect collision with tail
    for segment in tim.segments[1:]:
        if tim.head.distance(segment) < 15:
            board.update_high_score()
            tim.reset_snake()


screen.exitonclick()
