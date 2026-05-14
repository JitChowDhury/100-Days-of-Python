from turtle import Turtle,Screen

class Snake:
  
  def __init__(self):
    self.snake_segments=[]
    self.create_snake()
    self.angle=0
    self.head=self.snake_segments[0]

  def create_snake(self):
    self.xPos=0
    self.YPos=0
    for _ in range(3):
      self.add_segment((self.xPos,self.YPos))
      self.xPos-=20



  def add_segment(self,position):
    snake=Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    self.snake_segments.append(snake)

  def extend(self):
    self.add_segment(self.snake_segments[-1].position())
    

  def set_angle(self,angle):
    self.angle=angle


  def go_up(self):
    if self.snake_segments[0].heading()!=270:
      self.set_angle(90)
  def go_down(self):
    if self.snake_segments[0].heading()!=90:
      self.set_angle(270)
  def go_right(self):
    if self.snake_segments[0].heading()!=180:
      self.set_angle(0)
  def go_left(self):
    if self.snake_segments[0].heading()!=0:    
      self.set_angle(180)

  def move(self):
    for seg_num in range(len(self.snake_segments)-1,0,-1):
      newX=self.snake_segments[seg_num-1].xcor()
      newY=self.snake_segments[seg_num-1].ycor()
      self.snake_segments[seg_num].goto(newX,newY)
    self.snake_segments[0].setheading(self.angle)
    self.snake_segments[0].forward(20)

  def check_tail_collision(self):
    
    for seg in range(1,len(self.snake_segments)-1):
      if self.head.distance(self.snake_segments[seg])<10:
        return True
    return False

