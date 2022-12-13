from turtle import Turtle
Font = ("Courier", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, 270)
        self.write(align="center", arg=f"score: {self.score}", font=Font)
        self.hideturtle()
    def gameover(self):
        self.setposition(0, 0)
        self.write(align="center", arg=f"Game Over", font=Font)

    def addscore(self):
        self.clear()
        self.score += 1
        self.write(align="center",arg=f"score: {self.score}", font=Font)

