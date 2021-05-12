from data import question_data
from question_model import Question
from quiz import Quiz

question_bank = []
for q in question_data:
    question_text = q["question"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = Quiz(question_bank)

#while remaining_questions is true run next_question function from quiz.py
while quiz.remaining_questions():
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")