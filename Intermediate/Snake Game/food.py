from turtle import Turtle
import random


class Food:

    def __init__(self):
        self.food = Turtle(shape="circle")
        self.food.color("blue")
        self.food.penup()

    def get_food(self):
        return self.food

    def change_position(self):
        x = random.randint(-299, 299)
        y = random.randint(-299, 299)
        self.food.setpos(x, y)
