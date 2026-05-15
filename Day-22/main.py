from turtle import Screen , Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong!!!!")


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(5,1)
paddle.speed("fastest")
paddle.penup()
paddle.setposition(350,0)

def goup():
  posY=paddle.ycor()
  posY+=20
  paddle.setposition(350,posY)
def godown():
  posY=paddle.ycor()
  posY-=20
  paddle.setposition(350,posY)

screen.listen()

screen.onkey(goup,"w")
screen.onkey(godown,"s")


game_is_on=True
while game_is_on:
  screen.update()


screen.exitonclick()