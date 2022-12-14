from turtle import Turtle
Font = ("Courier", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, 270)
        self.write(align="center", arg=f"score: {self.score}   highscore: {self.highscore}", font=Font)
        self.hideturtle()
    def highestscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.clear()
        self.write(align="center", arg=f"score: {self.score}   highscore: {self.highscore}", font=Font)


    def addscore(self):
        self.clear()
        self.score += 1
        self.write(align="center", arg=f"score: {self.score}   highscore: {self.highscore}", font=Font)
