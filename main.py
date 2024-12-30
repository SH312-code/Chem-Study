import random # importing the random module for use in the generate_quiz function

def read_file(filename): #This function reads a file and extracts the data as a list seperated by the lines in the flies. 
    with open(filename, "r", encoding='utf-8') as f: # The use of the encoding functions is due to a problem with how the computer is storing some charcaters in the questions file, ie the characters do not have a incode conterpart, previos error message: UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 1248: character maps to <undefined>
        return f.read().splitlines()
#The below reads the 3 associated files and stores the data as lists
questions = read_file("questions.txt")
answers = read_file("answers.txt")
explain = read_file("explain.txt")
#There is no need to add a catch all due to the nature of how the files were made
question_set = []
wrong = []  # Define wrong as a global variable

def get_term_definition(): #This function creates an absrtact data type, the question, and adds it to the 'question set'. The question is formed by taking the nth ithem of each list and combining them in the order: question, answer, explaination
    for i in range(len(questions)):
        term = questions[i]
        definition = answers[i]
        explaniation = explain[i]
        question_set.append({"term": term, "definition": definition, "explaniation": explaniation})

def generate_quiz(): #This function is responceable for the creation of the questions and decides if they are right or wrong
    random.shuffle(question_set) #This makes the questions apper in a random order
    for index, question in enumerate(question_set): 
        print(f"\nQuestion {index + 1}: {question['term']}") #This displays the question, index + 1 is since the index actully starts at 0 for the first question, it is just for user clarity
        while True: # Within this loop it simpy asks the user for what thy belive the answer is. Every question in the question file is multiple choice so the answers are between 1 and 4. The reason to use a loop is to avoid an asnwer that is not within that range from breaking the code
            user_answer = input("Your answer (1-4): ")
            if user_answer in ['1', '2', '3', '4']: 
                break
            else:
                print("Invalid input. Please enter 1, 2, 3, or 4.")
        #This finds the correct answer to the question asked and its explaination
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
