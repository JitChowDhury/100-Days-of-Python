from turtle import Turtle , Screen
import pandas


turtle=Turtle()
screen = Screen()
screen.title("U.S.States Games")
screen.setup(725,491)
image="Day-25/Day-25-Final Game Proj/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


data = pandas.read_csv("Day-25/Day-25-Final Game Proj/50_states.csv")
states=data.state.to_list()

guessed_states=[]



while len(guessed_states)<50:
  answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct" , prompt="What's another state's name").title()

  if answer_state=="Exit":
      missing_states=[]
      for state in states:
        if state not in guessed_states:
          missing_states.append(state)
      new_data=pandas.DataFrame(missing_states)
      new_data.to_csv("Day-25/Day-25-Final Game Proj/StatesToLearn.csv")
      break
  if answer_state in states:
    guessed_states.append(answer_state)
    t=Turtle()
    t.hideturtle()
    t.penup()
    state_data=data[data.state==answer_state]
    t.goto(state_data.x.item(),state_data.y.item())
    t.write(answer_state)

