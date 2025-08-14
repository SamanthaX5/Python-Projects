import turtle
import time

# Window
wn = turtle.Screen()
wn.title("Pong - Turtle Edition")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddles
def make_paddle(x_pos):
    p = turtle.Turtle()
    p.speed(0)
    p.shape("square")
    p.color("white")
    p.shapesize(stretch_wid=5, stretch_len=1)
    p.penup()
    p.goto(x_pos, 0)
    return p

paddle_a = make_paddle(-350)
paddle_b = make_paddle(350)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# Center line
net = turtle.Turtle()
net.hideturtle()
net.speed(0)
net.color("gray")
net.penup()
net.goto(0, -300)
net.setheading(90)
for _ in range(30):
    net.pendown()
    net.forward(10)
    net.penup()
    net.forward(10)

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("0 : 0", align="center", font=("Courier", 24, "bold"))

def update_score():
    pen.clear()
    pen.write(f"{score_a} : {score_b}", align="center", font=("Courier", 24, "bold"))

PADDLE_STEP = 50

def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + PADDLE_STEP)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        paddle_a.sety(y - PADDLE_STEP)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + PADDLE_STEP)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        paddle_b.sety(y - PADDLE_STEP)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Help
def reset_ball(direction=1):
    ball.goto(0, 0)
    ball.dx = 4 * direction
    ball.dy = 4

FRAME_DELAY = 0.01

while True:
    wn.update()
    time.sleep(FRAME_DELAY)

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        score_a += 1
        update_score()
        reset_ball(direction=-1)

    if ball.xcor() < -390:
        score_b += 1
        update_score()
        reset_ball(direction=1)

    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        ball.dy += (ball.ycor() - paddle_b.ycor()) * 0.05

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        ball.dy += (ball.ycor() - paddle_a.ycor()) * 0.05