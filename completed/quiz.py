import time
import random

class Question:
    def __init__(self, prompt, answer, q_type='open', options=None):
        self.prompt = prompt
        self.answer = answer
        self.q_type = q_type
        self.options = options

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        random.shuffle(self.questions)
        print("Welcome")
        total_questions = len(self.questions)
        start_time = time.time() #12:50AM
        
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i + 1}/{total_questions}:")     #Q2/5 
            
            if question.q_type == 'multiple':
                print(question.prompt)
                for idx, option in enumerate(question.options, 1):
                    print(f"{idx}. {option}")
                USER_answer = input("Your answer (choose the number): ").strip()
                correct = (USER_answer == str(question.answer))
            elif question.q_type == 'true/false':
                print(f"{question.prompt} (True/False)") # IS EARTH ROUND (TRUE / FALSE) TRUE -> "T","R","U","E" True , TrUe -> true
                answer = input("Your answer: ").strip().lower()
                correct = (answer == question.answer.lower())
            else:
                print(question.prompt)
                answer = input("Your answer: ").strip()
                correct = (answer.lower() == question.answer.lower())#correct varriable will have TRUE / FAlSE as value
            
            if correct:
                self.score += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer was: {question.answer}")
        
        end_time = time.time()#1:0:30:35:04 AM - 12:50:25:15:48 AM
        elapsed_time = end_time - start_time
        print("\nQuiz Completed!")
        print(f"Your score: {self.score}/{total_questions}")
        print(f"Time taken: {elapsed_time:.2f} seconds")

# Example questions
questions = [
    Question("What is the capital of France?", "Paris"),
    Question("What is 2 + 2?", "4"),
    Question("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
    Question("What is the chemical symbol for water?", "H2O"),
    Question("Which planet is known as the Red Planet?", "Mars"),
    Question("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    Question("What is the largest mammal in the world?", "Blue Whale"),
    Question("What year did the Titanic sink?", "1912"),
    Question("Which language is primarily spoken in Brazil?", "Portuguese"),
    Question("True or False: The Great Wall of China is visible from space.", "False", 'truefalse'),
    Question("Which element has the atomic number 1?", "Hydrogen"),
    Question("Who is known as the 'Father of Computers'?", "Charles Babbage"),
    Question("Which country hosted the 2020 Summer Olympics?", "Japan"),
    Question("Which gas do plants absorb from the atmosphere?", "Carbon Dioxide"),
    Question("Multiple Choice: What is the capital of Japan?", "Tokyo", 'multiple', ["Kyoto", "Osaka", "Tokyo", "Nagoya"]),
    Question("Multiple Choice: Which of the following is a prime number?", "11", 'multiple', ["10", "11", "12", "14"])
]

# Creating the quiz
quiz = Quiz()

for q in questions:
    quiz.add_question(q)

# Starting the quiz
quiz.start()