from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_cars(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)

    def check_collision(self, player):
        for car in self.all_cars:
            if car.distance(player) < 20:
                return True
        return False
    
    def level_up(self):
        self.car_speed += 10

