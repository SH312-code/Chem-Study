import random

def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

questions = read_file("questions.txt")
answers = read_file("answers.txt")
explain = read_file("explain.txt")

question_set = []
wrong = []  # Define wrong as a global variable

def get_term_definition():
    for i in range(len(questions)):
        term = questions[i]
        definition = answers[i]
        explaniation = explain[i]
        question_set.append({"term": term, "definition": definition, "explaniation": explaniation})

def generate_quiz():
    random.shuffle(question_set)
    for index, question in enumerate(question_set):
        print(f"\nQuestion {index + 1}: {question['term']}")
        while True:
            user_answer = input("Your answer (1-4): ")
            if str(user_answer) in ['1', '2', '3', '4']:
                break
            else:
                print("Invalid input. Please enter 1, 2, 3, or 4.")

        correct_index = question['definition']
        correct_explaintion = question['explaniation']

        if user_answer == correct_index:
            print("Correct!, if you are unsure about how to answer the question, here is an explanation: \n", correct_explaintion)
        else:
            wrong.append(index)
            print(f"Incorrect. The correct answer is {correct_index} becuase {correct_explaintion}")
            
    print(f"\nYou got {len(question_set) - len(wrong)} out of {len(question_set)} correct.")
if __name__ == "__main__":
    get_term_definition()
    generate_quiz()
