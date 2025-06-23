"""
    main file
    - display game instuctions 
    - quiz level
    - start quiz
"""
from quiz_app import low_level_quiz, high_level_quiz

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
            - Your correct answers, incorrect answer and score are logged into a file for later review
            - Enter "q" to exit the program
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
            - Your correct answer, incorrect answer and score are logged into a file for later review
            - Do not enter a letter that is not in the option else it also considersed a failed quiz
            - Enter "q" to exit the progrma
            Happy playing \nGood luck
        """
    )
import time
def main():
    active = True
    while active:
        user_permission =  input("\nAre you ready to start the quiz (Y/N)? ").strip().lower()
        if user_permission == "n":
            print("You can start whenever you are ready to continue \nGood bye")
            active = False
        else:
            level = input("Choose a level you want to try(High/Low): ").strip().lower()

            if level == "high":
                print("Read the following instructions")
                show_instruction_high_levl()
                time.sleep(20)
                high_level_quiz()

            elif level == "low":
                print("Read the following instructions")
                show_instruction_low_levl()
                time.sleep(20)
                low_level_quiz()

            else:
                print("Still under construction")
                print("Choose either high or low to play")
                break

 # start quiz               
if __name__ == "__main__":
    main()
