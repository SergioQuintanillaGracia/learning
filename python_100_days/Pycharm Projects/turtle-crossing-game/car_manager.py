from turtle import Turtle
import random

from numpy.ma.core import true_divide

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
STARTING_TIME_BETWEEN_CAR_GENERATION = 0.4
DIFFICULTY_MULTIPLIER = 1.2


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_timer_max_value = STARTING_TIME_BETWEEN_CAR_GENERATION
        self.car_timer = self.car_timer_max_value
        self.move_distance = STARTING_MOVE_DISTANCE

    def update(self, frametime):
        self.car_timer -= frametime

        # Check if we should generate a new car
        if self.car_timer < 0:
            self.generate_car()
            self.car_timer = self.car_timer_max_value

        # Move the cars
        for car in self.cars:
            self.move(car)

    def move(self, car):
        new_x = car.xcor() - self.move_distance
        car.goto(new_x, car.ycor())

    def generate_car(self):
        rand_y = random.randint(-240, 240)
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1.5, stretch_len=2.5)
        car.color(random.choice(COLORS))
        car.goto(360, rand_y)
        self.cars.append(car)

    def position_collides_with_car(self, pos):
        # A car's width is 1.5 * 20 = 30px
        # We will count it as a collision if any car is at <= 30px from `pos`
        for car in self.cars:
            if car.distance(pos) < 30:
                return True

        return False

    def increase_difficulty(self):
        # Destroy every car turtle
        for car in self.cars:
            car.hideturtle()
            del car

        # Empty the list of car turtles
        self.cars = []

        self.car_timer_max_value /= DIFFICULTY_MULTIPLIER
        self.move_distance *= DIFFICULTY_MULTIPLIER