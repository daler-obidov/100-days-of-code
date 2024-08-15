import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_m = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_m.create_cars()
    car_m.move_cars()

    if car_m.check_collision(player):
        scoreboard.game_over()
        game_is_on = False
    if player.at_finish():
        player.to_start()
        scoreboard.increase_level()
        car_m.level_up()


screen.exitonclick()
