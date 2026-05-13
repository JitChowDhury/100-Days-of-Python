import random
from turtle import Turtle,Screen


# pointer = Turtle()
# screen=Screen()

# angle=0

# def forward():
#     pointer.forward(10)
# def backward():
#     pointer.backward(10)
# def counterClock():
#     global angle
#     angle+=5
#     pointer.setheading(angle)
# def clock():
#     global angle
#     angle-=5
#     pointer.setheading(angle)


# screen.listen()
# screen.onkey(forward,"w")
# screen.onkey(backward,"s")
# screen.onkey(counterClock,"a")
# screen.onkey(clock,"d")
# screen.onkey(screen.reset,"c")


# screen.exitonclick()




from turtle import  Turtle , Screen
is_game_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race?Enter a color: ")

colors = ["red","orange","yellow","green","blue","purple"]


y=-100
all_turtles=[]
for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.speed(0)
    tim.penup()
    tim.goto(-230,y)
    all_turtles.append(tim)
    y+=50

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_game_on=False
            if user_bet.lower()==turtle.color():
                print("You Won!")
            else:
                print("You Lost!!!")





screen.exitonclick()
print(user_bet)