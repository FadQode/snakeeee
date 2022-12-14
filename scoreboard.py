from turtle import Turtle
Font = ("Courier", 15, "normal")





class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore", mode="r") as file:
            a = file.read()
        self.highscore = int(a)
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, 270)
        self.write(align="center", arg=f"score: {self.score}   highscore: {self.highscore}", font=Font)
        self.hideturtle()
    def highestscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("highscore", mode="w") as file:
            file.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.write(align="center", arg=f"score: {self.score}   highscore: {self.highscore}", font=Font)


    def addscore(self):
        self.clear()
        self.score += 1
        self.write(align="center", arg=f"score: {self.score}   highscore: {self.highscore}", font=Font)

