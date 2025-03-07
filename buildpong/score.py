from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 30, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()