import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

# move turtle when we press the Up key
screen.onkey(key="Up", fun=player.move_turtle)

game_is_on = True


while game_is_on:
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with cars
    screen.update()

    # create and move the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 22:
            game_is_on = False
            scoreboard.game_over()
    #         print game over whenever the turtle collide with cars

    # Detect collision with wall
    if player.ycor() > 285:
        player.reset_turtle()
        car_manager.level_up_speed()
            #level up the speed of car whenever turtle collide with wall

        scoreboard.increase_level()
            #level up the score whenever turtle collide with the wall

screen.exitonclick()