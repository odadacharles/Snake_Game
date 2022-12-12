from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 12, 'bold')

with open("data.txt") as top_score:
    historic_high_score = int(top_score.read())


class Scoreboard(Turtle):
    """ Define a scoreboard class that writes and updates the score and also lets the player know when the game ends """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = historic_high_score
        self.penup()
        self.goto(10, 280)
        self.color('white')
        self.hideturtle()
        self.write(f"Score = {self.score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1

    def write_score(self):
        """ Method for updating the score on the screen """
        self.clear()
        self.write(f"Score = {self.score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score_file:
                high_score_file.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     """ Method for printing game over on the player screen """
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

