from snake import Snake
from food import Food
from scoreboard import Scoreboard
import window
import time

if __name__ == "__main__":
    game_is_on = True
    scr = window.init_screen()
    snk = Snake()
    food = Food()
    food.change_position()
    scrb = Scoreboard()
    while game_is_on:
        time.sleep(.1)
        scrb.print_score()
        scr.update()
        snk.snake_move()
        snk.detect_collision_with_food(food, scrb)
        snk.detect_collision_with_self()
        snk.snake_change_direction(scr)
        if not snk.get_game():
            scr.exitonclick()
