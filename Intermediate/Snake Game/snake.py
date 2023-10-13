from turtle import Turtle


class Snake:
    snakes = []
    game_going = True

    def __init__(self):
        for i in range(0, 3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.setposition(-20 * i, 0)
            self.snakes.append(snake)

    def get_snake(self):
        return self.snakes

    def add_more_snakes(self):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.setposition(self.snakes[len(self.snakes)-1].pos())
        snake.backward(20)
        self.snakes.append(snake)

    def update_positions(self, seg_num):
        self.snakes[seg_num].goto(self.snakes[seg_num - 1].xcor(), self.snakes[seg_num - 1].ycor())

    def snake_move(self):
        for num in range(len(self.snakes) - 1, 0, -1):
            self.update_positions(num)
        self.snakes[0].forward(20)
        self.detect_collision_with_wall()

    def go_up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def go_down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def go_left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def go_right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def snake_change_direction(self, screen):
        screen.listen()
        screen.onkey(self.go_up, "Up")
        screen.onkey(self.go_down, "Down")
        screen.onkey(self.go_left, "Left")
        screen.onkey(self.go_right, "Right")

    def has_wall_collision(self):
        return not -300 < self.snakes[0].pos()[0] < 300 and -300 < self.snakes[0].pos()[1] < 300

    def detect_collision_with_wall(self):
        if self.has_wall_collision():
            print("Game Over")
            self.game_going = False

        for i in range(1, len(self.snakes)):
            if self.snakes[0].pos() == self.snakes[i].pos():
                print("Game Over")
                self.game_going = False

    def snake_intersects_food(self, Food):
        return Food.get_food().pos()[0] - 20 < self.snakes[0].pos()[0] < Food.get_food().pos()[0] + 20 and Food.get_food().pos()[1] - 20 < self.snakes[0].pos()[1] < Food.get_food().pos()[1] + 20

    def detect_collision_with_food(self, Food, score):
        if self.snake_intersects_food(Food):
            Food.change_position()
            self.add_more_snakes()
            score.increase_score()
            food_on_snake = True
            while food_on_snake:
                for snake in self.snakes:
                    if snake.pos() == Food.get_food().pos():
                        Food.change_position()
                        food_on_snake = True
                    else:
                        food_on_snake = False

    def has_collision_with_self(self, i):
        return (self.snakes[i].pos()[0] - 5 < self.snakes[0].pos()[0] < self.snakes[i].pos()[0] + 5 and
                self.snakes[i].pos()[1] - 5 < self.snakes[0].pos()[1] < self.snakes[i].pos()[1] + 5)

    def detect_collision_with_self(self):
        for i in range(1, len(self.snakes)):
            if self.has_collision_with_self(i):
                self.game_going = False
                print("Gave Over")

    def get_game(self):
        return self.game_going
