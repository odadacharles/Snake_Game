from turtle import Turtle
import random


class Food(Turtle):
    """ Define a food class that inherits from the Turtle class"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.move()

    def move(self):
        """ Move the food to a random position within the screen """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
