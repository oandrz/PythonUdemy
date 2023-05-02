from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data["results"]:
    question_bank.append(Question(text=q["question"], answer=q["correct_answer"]))

brain = QuizBrain(list_question=question_bank)

while brain.still_has_questions():
    brain.next_question()
brain.quiz_finished()
