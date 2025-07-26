from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_all = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)  # Horizontal car
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_all.append(new_car)

    def move_cars(self):
        for car in self.car_all:
            car.backward(self.car_speed)
        # Remove cars that are off-screen
        self.car_all = [car for car in self.car_all if car.xcor() > -320]

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
