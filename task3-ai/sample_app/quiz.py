### Command-Line-Quiz application implemented by dcbrown and GPT-4o through duck.ai
### Initial prompt: "write an example program for a command-line based quiz app"

import random
import json
import os

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def to_dict(self):
        return {"prompt": self.prompt, "answer": self.answer}

    @staticmethod
    def from_dict(data):
        return Question(data['prompt'], data['answer'])

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == question.answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question.answer}\n")
    
    print(f"Your final score is {score}/{len(questions)}")

def create_quiz():
    questions = []
    while True:
        prompt = input("Enter the question (or type 'done' to finish): ")
        if prompt.lower() == 'done':
            break
        answer = input("Enter the answer (a single letter, e.g., 'a'): ")
        questions.append(Question(prompt, answer))

    quiz_name = input("Enter a name for your quiz: ")
    save_quiz(quiz_name, questions)

def save_quiz(quiz_name, questions):
    quiz_data = [question.to_dict() for question in questions]
    
    with open(f"{quiz_name}.json", "w") as file:
        json.dump(quiz_data, file)
    
    print(f"Quiz '{quiz_name}' saved successfully!")

def load_quiz(quiz_name):
    if os.path.exists(f"{quiz_name}.json"):
        with open(f"{quiz_name}.json", "r") as file:
            quiz_data = json.load(file)
            return [Question.from_dict(data) for data in quiz_data]
    else:
        print(f"No quiz found with the name '{quiz_name}'.")
        return []

def main():
    while True:
        print("1. Take a quiz")
        print("2. Create a new quiz")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            quiz_name = input("Enter the name of the quiz to take: ")
            questions = load_quiz(quiz_name)
            if questions:
                random.shuffle(questions)  # Shuffle questions
                run_quiz(questions)
        
        elif choice == '2':
            create_quiz()
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
