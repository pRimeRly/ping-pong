from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_player_score = 0
        self.right_player_score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=240)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f" {self.left_player_score}   :   {self.right_player_score}", align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.left_player_score += 1
        self.update_score()

    def increase_right_score(self):
        self.right_player_score += 1
        self.update_score()
