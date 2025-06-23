class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1} - {question.text} (True / False): ")

        self.check_answer(user_answer, question.answer)

        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Right!")
        else:
            print(f"Wrong. Correct answer: {correct_answer}")

        print(f"Current score: {self.score}/{self.question_number + 1}\n")