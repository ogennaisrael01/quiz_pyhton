"""
    main file
    - display game instuctions 
    - quiz level
    - start quiz
"""
from quiz_app import low_level_quiz_funtion, high_level_quiz_function

def show_instruction_high_levl():
    print(
        """
            Welcome to the quiz game  | High level
            How to play 
            - Each question will have four options 
            - You need to type the correct word (eg. water) as your answer 
            - After each question you will see if you were correct or not 
            - At the end you score will be displayed 
            - Answers are not case sensitive 
            - Your correct answers, incorrect answer and score are logged into a file

            Happy playing\n Good luck
        """
    )

def show_instruction_low_levl():
    print(
        """
            Welcome to the quiz game | Low level
            How to play
            - Each question will have four options
            - You will have to pick from the option display (A, B, C, D)
            - You can enter in upper or lower case. i.e they are not case sensitve
            - You will see if you are correct or not after each question
            - At the end score will be displayed
            - Your correct answer, incorrect answer and score are logged into a file
            Happy playing \nGood luck
        """
    )
import time
def main():
    active = True
    while active:
        user_permission =  input("Are you ready to start the quiz (Y/N)? ").strip().lower()
        if user_permission == "n":
            print("You can start whenever you are ready to continue \nGood bye")
            active = False
        else:
            level = input("Choose a level you want to try(High/Low): ").strip().lower()

            if level == "high":
                show_instruction_high_levl()
                time.sleep(20)
                high_level_quiz_function()

            if level == "low":
                show_instruction_low_levl()
                time.sleep(20)
                low_level_quiz_funtion()

            else:
                print("Still under construction")
                
if __name__ == "__main__":
    main()
