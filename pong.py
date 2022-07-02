import turtle as t
import random

player_a_score = 0
player_b_score = 0

# create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# Creating the left paddle
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("turtle")
leftPaddle.color("green")
leftPaddle.shapesize(stretch_wid=3, stretch_len=3)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

# Creating the right paddle
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("turtle")
rightPaddle.color("Red")
rightPaddle.tilt(180)
rightPaddle.shapesize(stretch_wid=3, stretch_len=3)
rightPaddle.penup()
rightPaddle.goto(350, 0)

# Code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("Blue")
ball.penup()
ball.goto(5, 5)
ball.dx = 0.2
ball.dy = 0.2

# Code for creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(10, 260)
pen.write("score", align="center", font=('Arial', 24, 'normal'))



# code for moving the leftpaddle
def leftpaddleup():
    y = leftPaddle.ycor()
    y += 90
    leftPaddle.sety(y)


def leftpaddledown():
    y = leftPaddle.ycor()
    y -= 90
    leftPaddle.sety(y)


# code for moving the rightpaddle
def rightpaddleup():
    y = rightPaddle.ycor()
    y += 90
    rightPaddle.sety(y)


def rightpaddledown():
    y = rightPaddle.ycor()
    y -= 90
    rightPaddle.sety(y)


# Assign keys to play
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border set up
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # Right width paddle Border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dy *= -1
        player_a_score += 1
        pen.clear()
        pen.write("Player A: {}                  Player B: {} ".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))
    # Left width paddle Border
    if (ball.xcor()) < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_b_score += 1
        pen.clear()
        pen.write("Player A: {}                 Player B: {} ".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))

    # Handling the collisions with paddles.

    if (340 < ball.xcor() < 350) and (rightPaddle.ycor() + 40 > ball.ycor() > rightPaddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (leftPaddle.ycor() + 40 > ball.ycor() > leftPaddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

