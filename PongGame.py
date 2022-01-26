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