# Pong (Left Hand vs Right Hand)
# By Max Acheson

import turtle

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
left_paddle.color("white")
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
right_paddle.color("white")
right_paddle.penup()
right_paddle.goto(370,0)