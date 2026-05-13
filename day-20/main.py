from turtle import Screen,Turtle
import time

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

xPos=0
YPos=0

snake_segments=[]

for _ in range(3):
  snake=Turtle(shape="square")
  snake.color("white")
  snake.penup()
  snake.setposition(xPos,YPos)
  snake_segments.append(snake)
  xPos-=20


is_game_on=True
while is_game_on:
  screen.update()
  time.sleep(0.1)
  
  for seg_num in range(len(snake_segments)-1,0,-1):
    newX=snake_segments[seg_num-1].xcor()
    newY=snake_segments[seg_num-1].ycor()
    snake_segments[seg_num].goto(newX,newY)
  snake_segments[0].right(90)
  snake_segments[0].forward(20)


screen.exitonclick()