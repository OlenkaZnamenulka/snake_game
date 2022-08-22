from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.whrite_score()

    def increase_score(self):
        self.score += 1

    def whrite_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Счет : {self.score}", align=ALIGMENT, font=FONT)
