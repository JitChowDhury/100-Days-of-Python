from turtle import Screen,Turtle
from snake import Snake
import time



screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# segment_1 = Turtle("square")
# segment_1.color('white')
#
# segment_2 = Turtle("square")
# segment_2.color('white')
# segment_2.goto(-20,0)
#
# segment_3 = Turtle("square")
# segment_3.color('white')
# segment_3.goto(-40,0)
snake = Snake()
screen.listen()

screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
isGameOn=True
while isGameOn:
    screen.update()
    snake.move()
    time.sleep(0.1)






















screen.exitonclick()