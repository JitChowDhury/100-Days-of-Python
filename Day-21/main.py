from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=ScoreBoard()
screen.listen()



screen.onkey(snake.go_up,"w")
screen.onkey(snake.go_down,"s")
screen.onkey(snake.go_right,"d")
screen.onkey(snake.go_left,"a")

is_game_on=True
while is_game_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  if snake.head.distance(food)< 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
  
  if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor()<-280 or snake.check_tail_collision():
    scoreboard.game_over()
    is_game_on=False


screen.exitonclick()