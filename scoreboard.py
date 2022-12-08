from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 12, 'bold')


class Scoreboard(Turtle):
    """ Define a scoreboard class that writes and updates the score and also lets the player know when the game ends """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(10, 280)
        self.color('white')
        self.hideturtle()
        self.write(f"Score = {self.score} ", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        """ Method for updating the score on the screen """
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score} ", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """ Method for printing game over on the player screen """
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

