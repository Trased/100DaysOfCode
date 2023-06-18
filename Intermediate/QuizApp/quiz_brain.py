class QuizBrain:
    def __init__(self, my_list):
        self.q_number = 0
        self.q_list = my_list
        self.correct_answers = 0

    def has_question(self):
        return self.q_number < len(self.q_list)

    def print_score(self):
        print(f"Your score is: {self.correct_answers} / {self.q_number+1}")

    def check_answer(self, answer):
        if self.q_list[self.q_number].answer == answer.title():
            print("You've got it right!")
            self.correct_answers += 1
        else:
            print("You've got it wrong :(")
        self.print_score()

    def next_question(self):
        pick = input(f"Q.{self.q_number + 1}: {self.q_list[self.q_number].text} True/False?")
        self.check_answer(pick)
        self.q_number += 1
        return pick
