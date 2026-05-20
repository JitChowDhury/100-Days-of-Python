from turtle import Turtle

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.score=0

    with open("Day-24/HighScore.txt") as file:
      content=file.read()
      self.highScore=int(content)



    self.color("white")
    self.hideturtle()
    self.penup()
    self.speed("fastest")
    self.goto(x=0,y=240)
    self.update_scoreboard()

  def increase_score(self):
    self.score+=1
    self.update_scoreboard()

  def reset(self):
    if self.score>self.highScore:
      self.highScore=self.score
      with open("Day-24/HighScore.txt", mode = "w") as file:
        file.write(str(self.highScore))
    self.score=0
    self.update_scoreboard()
    
  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.highScore}",align="center",font=("Courier",24,"normal"))

# with open("Day-24/HighScore.txt") as file:
#   content=file.read()
#   print(content)

# with open("Day-24/Food.txt" , mode="a") as file:
#   file.write("\nButter")