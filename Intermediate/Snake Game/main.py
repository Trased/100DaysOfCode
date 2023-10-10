#Initial commit, changes will be made.

import time
from turtle import Screen, Turtle


class Snake:
    turtles = []


def init_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen


def init_game_snake():
    turtles = []
    for i in range(0, 3):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.setposition(-20 * i, 0)
        turtles.append(turtle)
    return turtles


def update_positions(turtle, seg_num):
    return turtle[seg_num].goto(turtle[seg_num-1].xcor(), turtle[seg_num-1].ycor())


if __name__ == "__main__":
    game_is_on = True
    scr = init_screen()
    trt = init_game_snake()
    while game_is_on:
        scr.update()
        for num in range(len(trt) - 1, 0, -1):
            update_positions(trt, num)

        time.sleep(.2)

    scr.exitonclick()
