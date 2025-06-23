import time
import json
def load_from_quiz_file(file_name="quiz_file.json"):
    with open(file_name, "r") as file:
        try:
            data = json.load(file)
            return data
        except FileNotFoundError:
            print("Error: File not found")
import random    
def low_level_quiz_funtion():
    
    """
        A low level Quiz 
        - Loads questions from file
        - Presents multiple choice questions (A, B, C, D)
        - Tracks correct/incorrect answers and score
        - Saves results to files
    """ 
   
    quiz_question = load_from_quiz_file() #load question from file
    overrall_total_question = len(quiz_question) #total number of question
    correct_answers = [] #store correct answer in a dictionary
    incorrect_answers = [] #store incorrect answer in a dictionary
    score = 0 #Initialize the score
    total_question_answered_correctly = 0 # number of question a user answerd correctly
    total_question_answered = 0 # Total question answer

    random.shuffle(quiz_question)   
    for index, value in enumerate(quiz_question): # loop through question and display in a simple format
        print("=" * 50)
        print(f"Question {index} of {overrall_total_question}")
        question = value["question"]
        
        print (f"Question number {index}: {question}")

        # Display options to choose from 
        options = value["options"]
        for key, option in options.items(): # loop through options 
            print(f"{key}: {option}")
        print()
        print("Choose A, B, C, D from the above option")

            # get user answer
        user_answer = input("Enter your prefered answer: ").strip().upper()
        if  user_answer == value["answer"]:
            print("Correct!")
            correct_answers.append({"\nQuestion": value["question"], "Message": "Passed"})
            score += 1
            total_question_answered_correctly += 1

        
        else:
            print("Incorrect!")
            print(f"The correct answer is {value["answer"]}")
            incorrect_answers.append({"\nQuestion": value["question"], "Message": "Failed"})
    
        if index == 5:
            print("session  completed")
            break
        total_question_answered += 1
    
    # log scores into a txt file
    with open("score.txt", "w") as f:
        f.write(str(score))
    
    # log correct answer in a json file
    with open("correct_answer_file.json", "a") as file:
        json.dump(correct_answers, file)
    
    # log incorrect answer in a json file
    with open("incorrect_answer.json", "w") as file:
        file.write(str(incorrect_answers))
        
    # Resulta
    print(f"You answered {total_question_answered_correctly} out of {total_question_answered} correctly")        
    percentage = (score / total_question_answered ) * 100
    print(f"Your score is: {round(percentage, 2)}%")
low_level_quiz_funtion()


def high_level_quiz_function():
    """
        High level quiz function
        - Loads questions from file
        - User must type the answer (not multiple choice)
        - Tracks correct/incorrect answers and score
        - logs result to files
    """

    quiz_question = load_from_quiz_file() #load question from file
    overrall_total_question = len(quiz_question) #total number of question
    correct_answers = [] #store correct answer in a dictionary
    incorrect_answers = [] #store incorrect answer in a dictionary
    score = 0 #Initialize the score
    total_question_answered_correctly = 0 # number of question a user answerd correctly
    total_question_answered = 0 # Total question answer

    random.shuffle(quiz_question)
    for index, value in enumerate(quiz_question): # loop through question and display in a simple format
        print("=" * 50)
        print(f"Question {index} of {overrall_total_question}")
        question = value["question"]
        
        print (f"Question number {index}: {question}")

        options = value["options"]
        print("Provide the answers")
        

        user_answer = input("What is the correct answer: ").strip().capitalize()
        
        if user_answer == options[value["answer"]]:
            print("Correct!")
            correct_answers.append({"Question": value["question"], "Message": "Passed"})
            score += 1
            total_question_answered_correctly += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is {options[value["answer"]]}")
            incorrect_answers.append({"Question": value["question"], "Message": "Failed"})

        total_question_answered += 1
     # log scores into a txt file
    with open("score.txt", "a") as f:
        f.write(str(score))
    
    # log correct answer in a json file
    with open("correct_answer_file.json", "a") as file:
        json.dump(correct_answers, file, indent=2)
    
    # log incorrect answer in a json file
    with open("incorrect_answer.json", "a") as file:
        json.dump(incorrect_answers, file, indent=2)

    # Result
    print(f"You answered {total_question_answered_correctly} out of {total_question_answered} correctly")        
    percentage = (score / total_question_answered ) * 100
    print(f"Your score is: {round(percentage, 2)}%")
