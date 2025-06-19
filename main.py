import sys
import random
from termcolor import colored, cprint

questions = [
    {"question": "What is the capital city of Australia?", "answer": "Canberra"},
    {"question": "Which element has the chemical symbol 'O'?", "answer": "Oxygen"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "In which year did World War II end?", "answer": "1945"},
    {"question": "Which country is famous for the Eiffel Tower?", "answer": "France"},
    {"question": "How many continents are there on Earth?", "answer": "7"},
    {"question": "What is the main ingredient in guacamole?", "answer": "Avocado"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"question": "Who wrote the play'Romeo and Juliet'?", "answer": "William Shakespeare"}
]

def get_answer():
    answer = input("Your answer: ")
    return answer.strip()

def main():
    cprint("Welcome to Coomber's Quiz Game!", 'magenta')

    selected_questions = random.sample(questions, 5)

    score = 0
    for i, q in enumerate(selected_questions):
        cprint(f"\nQuestion {i + 1}:", 'cyan')
        print(f"Question: {q['question']}")
        answer = get_answer()
        if answer.lower() == q["answer"].lower():
            cprint("Correct!", 'green')
            score += 1
        else:
            cprint(f"Incorrect! The correct answer is: {q['answer']}", 'red')
    cprint(f"\nYour final score is: {score}/5", 'yellow')

if __name__ == "__main__":
    main()
