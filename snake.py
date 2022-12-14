import turtle as t
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.make_a_snake()
        self.head = self.snake_body[0]

    def make_a_snake(self):
        self.x = 0
        for i in range(3):
            self.add_segment()

    def add_segment(self):
        ular = t.Turtle(shape="square")
        ular.setposition(self.x - 20, ular.ycor())
        ular.penup()
        ular.color("white")
        self.x -= 20
        self.snake_body.append(ular)

    def extend(self):
        ular = t.Turtle(shape="square")
        ular.setposition(self.snake_body[-1].position())
        ular.penup()
        ular.color("white")
        self.snake_body.append(ular)

    def losing(self):
        for ular in self.snake_body:
            ular.goto(1000, 1000)
        self.snake_body.clear()
        self.make_a_snake()
        self.head = self.snake_body[0]

    def snake_move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(20)
    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)
    def snake_down(self):
        if self.head.heading() != UP:
            self.head.seth(270)
    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)
    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)