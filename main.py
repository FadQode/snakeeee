import turtle as t
import time as ti
import snake as s
import food
import scoreboard

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
python = s.Snake()
food = food.Food()
score = scoreboard.Score()

screen.onkey(fun=python.snake_up, key="Up")
screen.onkey(fun=python.snake_down, key="Down")
screen.onkey(fun=python.snake_right, key="Right")
screen.onkey(fun=python.snake_left, key="Left")

game = True
while game:
    screen.update()
    ti.sleep(0.08)
    python.snake_move()
    screen.update()
    if python.head.distance(food) < 15:
        food.refresh()
        python.extend()
        score.addscore()
    if python.head.xcor() < -280 or python.head.xcor() > 280 or python.head.ycor() < -280 or python.head.ycor() > 280:
        score.gameover()
        game = False
    for body in python.snake_body[1:]:
        if python.head.distance(body) < 10:
            score.gameover()
            game = False
screen.exitonclick()
