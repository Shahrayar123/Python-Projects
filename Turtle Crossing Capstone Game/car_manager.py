from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5




class CarManager(Turtle):
#   class to manage the blocks


    def __init__(self):
        # creating a list of cars

        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # method to create a car

        random_chance = random.randint(1, 6)

        if random_chance == 1:
            """
            By this the car will be created only when 1 will come so there will be some distance between the 
            cars where out turtle can move.
            """


            new_car = Turtle()

            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            y_cor = random.randint(-250, 250)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)


    def move_car(self):
#       method to move the car

        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up_speed(self):
        # level up speed everytime the turtle hits the wall

        self.car_speed += MOVE_INCREMENT


