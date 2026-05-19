from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!!!!")

screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

screen.listen()

screen.onkeypress(l_paddle.goup, "w")
screen.onkeypress(l_paddle.godown, "s")

screen.onkeypress(r_paddle.goup, "Up")
screen.onkeypress(r_paddle.godown, "Down")

game_is_on = True

while game_is_on:

    time.sleep(0.1)

    ball.Move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # Paddle collision
    if (
        l_paddle.distance(ball) < 50 and ball.xcor() < -330
    ) or (
        r_paddle.distance(ball) < 50 and ball.xcor() > 330
    ):
        ball.bounceX()

    # Missed ball
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset()

    screen.update()

screen.exitonclick()