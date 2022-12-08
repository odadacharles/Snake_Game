from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """ Define snake class that initialises the snake in the game"""
    def __init__(self):
        self.num_seg = 3
        self.start_pos = 0
        self.segments = []
        self.new_snake()
        self.head = self.segments[0]

    def new_snake(self):
        """ Method for creating a new snake """
        for segment in range(0, self.num_seg):
            new_segment = Turtle(shape='square')
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=self.start_pos, y=0)
            self.start_pos -= 20
            self.segments.append(new_segment)

    def add_segment(self):
        """ Method for adding new segments to the snake """
        position = (self.segments[-1].position())
        add_seg = Turtle(shape='square')
        add_seg.color('white')
        add_seg.penup()
        add_seg.goto(position)
        self.segments.append(add_seg)

    def move_snake(self):
        """ Method that defines how the snake moves around the screen """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """ Method that defines what happens when the 'up' button is pressed """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ Method that defines what happens when the 'down' button is pressed """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ Method that defines what happens when the 'right' button is pressed """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ Method that defines what happens when the 'left' button is pressed """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
