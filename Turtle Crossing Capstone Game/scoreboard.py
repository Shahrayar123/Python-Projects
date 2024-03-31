from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
#     class to get hold of scoreboard

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
    #     Increase the level when turtle hits the wall

        self.level += 1
        self.update_scoreboard()

    def game_over(self):

        self.goto(0, 0)
        self.write("Game Over!!", align="center", font=FONT)