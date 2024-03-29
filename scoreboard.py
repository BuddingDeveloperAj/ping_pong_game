from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 230)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}   {self.r_score}", align='center', font=('Arial', 50, 'bold'))

    def increase_l_score(self):
        self.l_score += 1
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.update_score()
