from q_data import question_data
import random

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


# define question bank
question_bank = []

# fill question bank with question objects
for i in range(len(question_data)):
    qi = Question(question_data[i]['text'], question_data[i]['answer'])
    question_bank.append(qi)


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.number_of_questions = len(q_list)

    # next question method
    def next_question(self):
        # increment every time a new question is randomly picked.
        self.question_number += 1

        # randomly pick a question from the list and remove it from there
        current_question = random.choice(self.question_list)
        self.question_list.remove(current_question)

        # check if there are still questions in the question bank
        if len(self.question_list) != 0:
            print(f"Q{self.question_number} {current_question.text}")
            # make sure the user types either 'true' or 'false'. case insensitive
            while True:
                user_ans = input("What do you think? True or False ").lower().strip()
                if user_ans == 'true' or user_ans == 'false':
                    break
                else:
                    continue
            # if correct answer, score increase
            if user_ans == current_question.answer.lower():
                self.score += 1
                print("That's right!")
            else:
                print("Wrong answer.")

        # no more questions in the bank
        else:
            print(f"no more questions. Your score is {self.score} out of {self.number_of_questions}")
            exit()


# Play a game. Instantiate a new game.
igra = QuizBrain(question_bank)

while True:
    igra.next_question()




