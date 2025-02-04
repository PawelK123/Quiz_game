from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    text = i["text"]
    answer = i["answer"]
    new_question = Question(text,answer)
    question_bank.append(new_question)
Quiz = QuizBrain(question_bank)
while Quiz.still_has_question():
    Quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was {Quiz.score}/{Quiz.question_number}")