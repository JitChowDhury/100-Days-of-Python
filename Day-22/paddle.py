from turtle import Turtle


class Paddle(Turtle):

  def __init__(self,position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(5,1)
    self.speed("fastest")
    self.penup()
    self.setposition(position)

  def goup(self):
    posY=self.ycor()
    posY+=20
    self.setposition(self.xcor(),posY)
    print("working")
  def godown(self):
    posY=self.ycor()
    posY-=20
    self.setposition(self.xcor(),posY)
    print("working")



