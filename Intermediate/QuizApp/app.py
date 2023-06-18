from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
if __name__ == "__main__":
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"]))

    q_brain = QuizBrain(question_bank)
    while q_brain.has_question():
        q_brain.next_question()
    

