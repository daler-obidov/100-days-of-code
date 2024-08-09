from turtle import Turtle, Screen

mike = Turtle()


screen = Screen()
screen.bgcolor('DarkBlue')
mike.color("red")
mike.pensize(4)


def move_f():
    mike.forward(10)
def move_b():
    mike.bk(10)
def move_right():
    mike.right(10)
def move_left():
    mike.left(10)
def clear():
    mike.clear()
    mike.penup
    mike.home
    mike.pendown
    
screen.listen()
screen.onkey(key='s', fun=move_b)
screen.onkey(key='w', fun=move_f)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='c', fun=clear)


screen.exitonclick()