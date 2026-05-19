from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.width=20
    self.height=20
    self.setposition(0,0)
    self.shape("circle")
    self.penup()
    self.color("white")
    self.x_vel=10
    self.y_vel=10
    

  def Move(self):

    new_x=self.xcor()+self.x_vel
    new_y=self.ycor()+self.y_vel

    self.goto(new_x,new_y)

  def bounceX(self):
      self.x_vel=-self.x_vel
      
  def bounceY(self):
     self.y_vel=-self.y_vel
  
  def reset(self):
      self.goto(0,0)
      self.bounceX()
      

