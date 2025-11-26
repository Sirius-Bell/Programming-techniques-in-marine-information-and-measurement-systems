import turtle
import time

# Окно
win = turtle.Screen()
win.title("Пинг-понг — простой")
win.setup(width=800, height=600)
win.bgcolor("black")
win.tracer(0)

# Левый ракетка
left = turtle.Turtle()
left.shape("square")
left.color("white")
left.shapesize(stretch_wid=5, stretch_len=1)
left.penup()
left.goto(-350, 0)

# Правый ракетка
right = turtle.Turtle()
right.shape("square")
right.color("white")
right.shapesize(stretch_wid=5, stretch_len=1)
right.penup()
right.goto(350, 0)

# Мяч
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.18
ball.dy = 0.18

# Счёт
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write(f"{score_a} : {score_b}", align="center", font=("Courier", 24, "normal"))

# Управление
def left_up():
    y = left.ycor() + 20
    if y > 250: y = 250
    left.sety(y)

def left_down():
    y = left.ycor() - 20
    if y < -250: y = -250
    left.sety(y)

def right_up():
    y = right.ycor() + 20
    if y > 250: y = 250
    right.sety(y)

def right_down():
    y = right.ycor() - 20
    if y < -250: y = -250
    right.sety(y)

win.listen()
win.onkeypress(left_up, "w")
win.onkeypress(left_down, "s")
win.onkeypress(right_up, "Up")
win.onkeypress(right_down, "Down")

# Главный цикл
while True:
    win.update()
    time.sleep(1/1000)

    # движение мяча
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # границы по Y
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # если мяч ушёл за правую сторону — очко левому
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write(f"{score_a} : {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # если мяч ушёл за левую сторону — очко правому
    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write(f"{score_a} : {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Столкновение с правой ракеткой
    if (340 < ball.xcor() < 350) and (right.ycor() - 50 < ball.ycor() < right.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    # Столкновение с левой ракеткой
    if (-350 < ball.xcor() < -340) and (left.ycor() - 50 < ball.ycor() < left.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
