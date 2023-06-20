from turtle import Turtle, Screen
import random
screen = Screen()
pick = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color: ").lower()

colors = ["purple", "blue", "green", "yellow", "orange", "red"]
turtles = []
pos = 125
for i in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.resizemode("user")
    turtle.shapesize(2, 2)
    turtle.penup()
    turtle.setposition(-450, pos)
    turtles.append(turtle)
    pos -= 50


game_on = True
while game_on:
    for turtle in turtles:
        dist = random.randint(0, 10)
        turtle.forward(dist)
        if turtle.xcor() > 450:
            if pick == turtle.fillcolor():
                print("Congratulations! You've made the correct pick!")
            else:
                print(f"Whoops! Your turtle lost... the {turtle.fillcolor()} turtle wins")
            game_on = False
            screen.bye()
            break
