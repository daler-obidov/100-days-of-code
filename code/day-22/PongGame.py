from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

def check_collision(ball, paddle):

    return (ball.xcor() > paddle.xcor() - 10 and ball.xcor() < paddle.xcor() + 10 and
            ball.ycor() < paddle.ycor() + 50 and ball.ycor() > paddle.ycor() - 50)

def main():
    screen = Screen()
    screen.bgcolor('black')
    screen.setup(height=600, width=800)
    screen.title("Pong")
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.go_up, 'Up')
    screen.onkey(r_paddle.go_down, 'Down')
    screen.onkey(l_paddle.go_up, 'w')
    screen.onkey(l_paddle.go_down, 's')

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()

        ball.move()

        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_y()

        if check_collision(ball, r_paddle) or check_collision(ball, l_paddle):
            ball.bounce_x()

        if ball.xcor() > 390:
            ball.reset_position()
            ball.bounce_x()
            scoreboard.l_point()

        if ball.xcor() < -390:
            ball.reset_position()
            ball.bounce_x()
            scoreboard.r_point()

    screen.exitonclick()

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

def check_collision(ball, paddle):
    """ Check for collision between ball and paddle """
    return (ball.xcor() > paddle.xcor() - 10 and ball.xcor() < paddle.xcor() + 10 and
            ball.ycor() < paddle.ycor() + 50 and ball.ycor() > paddle.ycor() - 50)

def main():
    screen = Screen()
    screen.bgcolor('black')
    screen.setup(height=600, width=800)
    screen.title("Pong")
    screen.tracer(0)  # Turn off animation to manually control updates

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.go_up, 'Up')
    screen.onkey(r_paddle.go_down, 'Down')
    screen.onkey(l_paddle.go_up, 'w')
    screen.onkey(l_paddle.go_down, 's')

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()

        ball.move()

        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_y()

        if check_collision(ball, r_paddle) or check_collision(ball, l_paddle):
            ball.bounce_x()

        if ball.xcor() > 390:
            ball.reset_position()
            ball.bounce_x()
            scoreboard.l_point()

        if ball.xcor() < -390:
            ball.reset_position()
            ball.bounce_x()
            scoreboard.r_point()

    screen.exitonclick()

if __name__ == "__main__":
    main()
