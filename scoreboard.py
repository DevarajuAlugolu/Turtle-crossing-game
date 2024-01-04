from turtle import Turtle


FONT=("Courier",24,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_no=1
        self.color("white")
        self.penup()
        self.hideturtle()

    def level(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"level :{self.level_no}",align="left",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)


