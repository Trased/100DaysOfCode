from turtle import Turtle, Screen
import pandas

scr = Screen()
scr.setup(width=725, height=491)
scr.bgpic("blank_states_img.gif")
scr.title("States Guess Game")
scr.tracer(0)
csv_input = pandas.read_csv("50_states.csv")
states = csv_input["state"]
coordinates = []
state_list = []
for i in range(0, len(states)):
    coordinates.append((csv_input["x"][i], csv_input["y"][i]))
    state_list.append(states[i])
game_is_on = True
while game_is_on:
    for i in range(0, 50):
        answer = scr.textinput(f"{i}/50 States Correct", "What's another state name?:")
        if answer in state_list:
            trt = Turtle()
            trt.color("Black")
            trt.hideturtle()
            trt.penup()
            trt.goto(coordinates[state_list.index(answer)])
            trt.write(answer)
        else:
            ans = scr.textinput("You Lost", "Do you want to retry? Y/N")
            if ans != "Y":
                game_is_on = False
                break
