from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.bgcolor("DarkBlue")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "white", "purple"]
y = [-70, -40, -10, 20, 50, 80]
turtles = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230 , y=y[index])
    turtles.append(new_turtle)


if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            win = turtle.pencolor()
            if win == user_bet:
                print(f"You've won! The {win} turtle is the winner!")
            else:
                print(f"You've lost! The {win} turtle is the winner!")


        random_d = random.randint(0,10)
        turtle.forward(random_d)
    





















screen.exitonclick()