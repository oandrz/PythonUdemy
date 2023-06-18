import random

from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_collection = []
        self.moving_distance = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            car = Car(random.choice(COLORS), (300, random.randint(-250, 250)))
            self.car_collection.append(car)

    def move_cars(self):
        for car in self.car_collection:
            car.move_forward(self.moving_distance)

    def add_speed(self):
        self.moving_distance += MOVE_INCREMENT

    def detect_collision(self, player):
        for car in self.car_collection:
            if car.distance(player) <= 20:
                return True

        return False



