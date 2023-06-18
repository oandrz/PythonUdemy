class QuizBrain:

    def __init__(self, list_question):
        self.question_number = 0
        self.user_score = 0
        self.question_list = list_question

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number = self.question_number + 1
        user_answer = input(f"Q.{self.question_number} {question.text} (True/False)?:")
        self.check_answer(user_answer=user_answer, correct_answer=question.answer)

    def still_has_questions(self):
        try:
            self.question_list[self.question_number]
        except IndexError:
            return False

        return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You're right")
            self.user_score += 1
        else:
            print("You're wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"You're current score is: {self.user_score}/{self.question_number}")

    def quiz_finished(self):
        print("You've completed the quiz")
        print(f"You're final score was: {self.user_score}/{self.question_number}")



