# Pong (Left Hand vs Right Hand)
# By Max Acheson

import turtle
import winsound

game_window = turtle.Screen()
game_window.title("Pong by Max")
game_window.bgcolor("black")
game_window.setup(width=800, height=600)
game_window.tracer(0)

# Coding for Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.color("red")
left_paddle.penup()
left_paddle.goto(-370,0)

# Left Paddle Movement
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# Left Paddle Key Binds
game_window.listen()
game_window.onkeypress(left_paddle_up, "q")
game_window.onkeypress(left_paddle_down, "a")

# Coding for Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.color("blue")
right_paddle.penup()
right_paddle.goto(370,0)

# Right Paddle Movement
def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Right Paddle Key Binds
game_window.listen()
game_window.onkeypress(right_paddle_up, "o")
game_window.onkeypress(right_paddle_down, "l")

# Pong Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

# Scoreboard
score_writer = turtle.Turtle()
score_writer.speed(0)
score_writer.color("White")
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0,260)
score_writer.write("Left Hand: 0      Right Hand: 0", align="center", font=("courier", 18, "normal"))

# Scoring Mechanism
left_score = 0
right_score = 0

# Main Loop
while True:
    game_window.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Parameters
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -283:
        ball.sety(-283)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        left_score += 1
        score_writer.clear()
        score_writer.write("Left Hand: {}      Right Hand: {}".format(left_score, right_score), align="center", font=("courier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        right_score += 1
        score_writer.clear()
        score_writer.write("Left Hand: {}      Right Hand: {}".format(left_score, right_score), align="center", font=("courier", 18, "normal"))
    
    # Collision Mechanics
    if (ball.xcor() > 350 and ball.xcor() < 370) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() -40):
        ball.setx(350)
        ball.dx *= -1
        winsound.PlaySound("bonk.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -350 and ball.xcor() > -370) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() -40):
        ball.setx(-350)
        ball.dx *= -1
        winsound.PlaySound("bonk.wav", winsound.SND_ASYNC)