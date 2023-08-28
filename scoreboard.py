from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 22, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = 0
        self.high_score = int(self.read_high_score())
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.pencolor("white")
        self.penup()
        self.fillcolor("black")
        self.set_score()

    def set_score(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"Score:   {self.point} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increment_score(self):
        self.point += 1
        self.clear()

    def reset(self):
        if self.point > self.high_score:
            self.high_score = self.point
            self.write_high_score()
        self.point = 0

    def read_high_score(self):
        with open("data.txt") as file:
            return file.read()

    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.point))
