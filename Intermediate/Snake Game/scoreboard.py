from turtle import Turtle
class Scoreboard:

    def __init__(self):
        self.score = 0
        self.score_text = Turtle()
        self.score_text.color("White")
        self.score_text.hideturtle()
        self.score_text.penup()
        self.score_text.goto(0, 250)

    def increase_score(self):
        self.score += 1

    def print_score(self):
        self.score_text.clear()
        self.score_text.write("Score = " + str(self.score), False, "Center", ("Arial", 20, "normal"))
