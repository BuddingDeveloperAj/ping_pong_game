from turtle import Turtle


class Separator(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.dashed_line()


    def dashed_line(self):
        while self.ycor() < 350:
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)
