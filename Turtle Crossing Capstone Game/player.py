from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
        # class to create the turtle

        def __init__(self):
            super().__init__()
            self.shape("turtle")
            self.penup()
            self.goto(STARTING_POSITION)
            self.setheading(90)

        def move_turtle(self):
            # method to move the turtle

            self.forward(MOVE_DISTANCE)

        def reset_turtle(self):
            # method to reset the turtle to move it original position when hit the wall

            self.goto(STARTING_POSITION)