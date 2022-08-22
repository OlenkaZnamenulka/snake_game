from turtle import Turtle
MOVE_DISTANCE = 20
FORWARD = 0
BACK = 180
LEFT = 90
RIGHT = 270
NUMBER_SEGMENTS = 3


class Snake:
    def __init__(self):
        self.segments = []

        x = 0
        for _ in range(NUMBER_SEGMENTS):
            self.creat_turtle(x, 0)
            x -= 20
        self.head = self.segments[0]

    def creat_turtle(self, x_coor: int, y_coor: int):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(x_coor, y_coor)
        self.segments.append(turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[seg_num - 1].xcor()
            ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(xcor, ycor)
        self.segments[0].forward(MOVE_DISTANCE)

    def turn_forward(self):
        if self.head.heading() != BACK:
            self.head.setheading(FORWARD)

    def turn_back(self):
        if self.head.heading() != FORWARD:
            self.head.setheading(BACK)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self):
        x_cor, y_cor = self.segments[-1].position()
        self.creat_turtle(x_cor, y_cor)


