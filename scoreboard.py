from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 22, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = 0
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.pencolor("white")
        self.penup()
        self.fillcolor("black")
        self.set_score()

    def set_score(self):
        self.goto(0, 270)
        self.write("Score: " + str(self.point), True, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increment_score(self):
        self.point += 1
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
