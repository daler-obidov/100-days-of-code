from turtle import Turtle, Screen
import turtle as t
import random
# import turtle
# from turtle import *
# import turtle as t

screen = Screen()
screen.bgcolor("DarkBlue")

mike = Turtle()
mike.shape("classic")
mike.color("red")
# mike.pensize(5)
mike.speed(11)
# def shape(num_sides):
#     for i in range(num_sides):
#         angle = 360 / num_sides
#         mike.forward(100)
#         mike.right(angle)
t.colormode(255)
def random_cl():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color
def spirograph(size):
    for i in range(int(360 / size)):
        mike.color(random_cl())
        mike.circle(100)
        current_h = mike.heading()
        mike.setheading(current_h + size)
        mike.circle(100)
spirograph(10)


# directions = [0, 90, 180, 270]

# for shape_in in range(250):
#     mike.color(random_cl())
#     mike.forward(40)
#     mike.setheading(random.choice(directions))
    # shape(shape_in)

    # mike.penup()
    # mike.forward(10)
    # mike.pendown()


screen.exitonclick()


