from turtle import  Turtle
from turtle import  Screen
import  random

heli = Turtle()
heli.shape(name="turtle")
heli.color("green")

colors=["orange red","yellow green","medium aquamarine","dodger blue","medium slate blue"]

num_side=3
angle=360/num_side

# for _ in range(num_side):
#     heli.pendown()
#     heli.forward(10)
#     heli.penup()
#     heli.forward(10)


while num_side < 10:
    for _ in range(num_side):
        angle = 360 / num_side
        heli.forward(100)
        heli.right(angle)
    num_side+=1
    heli.color(random.choice(colors))




















screen=Screen()
screen.title("TurtleGame")
screen.exitonclick()