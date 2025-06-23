
import json
import random
import time
from json import JSONDecodeError

# Read quiz question from a json file
def load_from_quiz_file(file_name="quiz_file.json"):
    with open(file_name, "r") as file:
        try:
            data = json.load(file)
            return data
        except JSONDecodeError:
            print("Error: File not found")

#save correct answers into a json file for later review
def save_correct_answers(answer, filename="correct_answer_file.json"):
    """
        - Saves the questions that you passed
        - A message indicating that you passed that question
    """
    try:
        with open(filename, "w") as file:
            json.dump(answer, file)
    except JSONDecodeError as e:
        print(f"Error: {e}")

# Save incorrect answer into a json file for later review
def save_incorrect_answer(answer, filename="incorrect_answer.json"):
    """
        - Saves the question that you passeed
        - A message indicating that you failed the question
        - Your answer to that question
        - The correct answer
    """
    try:
        with open(filename, "w") as file:
            json.dump(answer, file)
    except JSONDecodeError as e:
        print(f"Error: {e}")

total_quiz = len(load_from_quiz_file())

def load_question():
    """
     - Load questions from JSON file
    """
    questions = load_from_quiz_file()
    random.shuffle(questions)
    for question in questions:
        yield question
    

def low_level_quiz():

    """
        A low level Quiz 
        - Loads questions from file
        - Presents multiple choice questions (A, B, C, D)
        - Tracks correct/incorrect answers and score
        - Saves results to files
    """ 
    quiz_question = load_question()
    correct_answers = []
    incorrect_answers = []

    for index, value in enumerate(quiz_question):
        print("=" * 50)
        print(f"This is question number {index} out of {total_quiz}")
        # Display question one at a time
        question = value["question"]
        print(f"\nQuestion: {question}")

        # Display options
        options = value["options"]
        for key, option in options.items():
           print(f"{key}: {option}") 

        print("Choose an answer from the above options")

        # Get an answer from a user
        user_answer = input("Enter your prefered choice(a, b, c, d) ").strip().upper()

        # Checks if a user enter a valid option, else it is considered a failed test
        if user_answer == "Q":
            print("\nThank you for playing \nYou can always restart the program")
            break
        elif user_answer not in options.keys():
            print("Failed.\nPlease enter a valid option next time(a, b, c, d) ")
            incorrect_answers.append({"Question": value["question"], "Message": "Failed: Entered invaliid option"})

        elif user_answer ==  value["answer"]: # compares user answer to the correct answer
            print("That is correct")
            correct_answers.append({"Question": value["question"], "Message": "Passed"})

        else: # the answer was wrong but in list of options
            print("Incorrect!")
            print(f"The correct answer is {value["answer"]}")
            incorrect_answers.append({"Question": value["question"], "Message": "Failed", "Your answer": user_answer, "Correct answer": value["answer"]})

        score = len(correct_answers)
        total_question_answered = score + len(incorrect_answers)
    
    save_correct_answers(correct_answers) 
    save_incorrect_answer(incorrect_answers)
    print("\nResult loading......")
     # Result
    time.sleep(10)
    print(f"\nYou answered {score} out of {total_question_answered} correctly")        
    percentage = (score / total_question_answered ) * 100
    print(f"Your score is: {round(percentage, 2)}%")


def high_level_quiz():

    """
        High level quiz function
        - Loads questions from file
        - User must type the answer (not multiple choice)
        - Tracks correct/incorrect answers and score
        - logs result to files
    """
    questions = load_question()
    correct_answers = []
    incorrect_answers = []

    for index, value in enumerate(questions): 
        print("=" * 50)

        # Get question
        question = value["question"]
        
        print (f"Question {index}: {question}")

        options = value["options"]
        
        user_answer = input("\nYou are required to enter the correct answer\n " ).strip().capitalize()
        # compare user answer with the correct answer 
        if user_answer == options[value["answer"]]:
            print("That is correct!")
            correct_answers.append({"Question": value["question"], "Message": "Passed"})
        elif user_answer == "Q":
            print("Thank you for playing \nYou can always restart the program")
            break
        else:
            print("Incorrect!")
            print(f"The correct answer is {options[value["answer"]]}")
            incorrect_answers.append({"Question": value["question"], "Message": "Failed", "Your answer": user_answer, "Correct Answer": value["answer"]})
        
        score = len(correct_answers)
        total_question_answered = score + len(incorrect_answers)
    
    save_correct_answers(correct_answers) 
    save_incorrect_answer(incorrect_answers)
    print("\nResult loading......")
     # Result
    time.sleep(10)
    print(f"\nYou answered {score} out of {total_question_answered} correctly")        
    percentage = (score / total_question_answered ) * 100
    print(f"Your score is: {round(percentage, 2)}%")
