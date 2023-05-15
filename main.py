import time
from colorama import init, Fore, Style
import json
from inputimeout import inputimeout, TimeoutOccurred
import random
import pytest

# Initialize colorama
init(autoreset=True)

# Allows access to JSON
with open('test_question.json') as f:
    test_question = json.load(f)

# Defines
def display_question(question):
    print(Fore.YELLOW + question['question'])
    print(Fore.BLUE + "Hint:", question['hint'])
    for index, option in enumerate(question['options']):
        print(Fore.CYAN + f"{index + 1}. {option}")
    print(Style.RESET_ALL)

# Defines the total number of questions
def total_questions():
    return len(test_question['test_question'])

# Function to shuffle the questions into random orders 
def shuffle_questions():
    random.shuffle(test_question['test_question'])

# Defines
def run_driver_test():
    score = 0
    incorrect_answers = []

    print(Fore.GREEN + "Welcome to LetsDrive! the VIC Drivers Learner Test Practice app! Input your name to start")
    my_name = input()
    print('Hello, ' + my_name + ' today you\'ll be taking a practice driver\'s test which will help you prepare for the real thing. You will have 32 minutes (1 minute per question) to complete this test and must answer at least 26 out of the 32 questions correctly.')
    print("Let's begin!\n")

    # Gives the reader time to read the description before the test starts
    time.sleep(3)

    # Shuffle the questions
    shuffle_questions()

    # Iterate through the questions and implement the inputimeout function
    for question in test_question['test_question']:
        display_question(question)
        try:
            user_answer = inputimeout(prompt=Fore.WHITE + "Enter answer A, B, C: ", timeout=60)
            user_answer = user_answer.strip().upper()

            # Check the answer
            if user_answer == question['answer'].upper():
                score += 1
                print(Fore.GREEN + "Correct!")
            else:
                incorrect_answers.append(question)
                print(Fore.RED + "Incorrect!")
        except TimeoutOccurred:
            print(Fore.RED + "Time's up! Moving on to the next question.")
            incorrect_answers.append(question)
        except Exception as e:
            print(Fore.RED + "An error occurred:", str(e))
            incorrect_answers.append(question)

        print()

    # Calculates the user's score and whether it's a passing score
    passing_score = int(0.8 * total_questions())

    print(Fore.BLUE + "Test complete, " + my_name + "!")
    print(Fore.CYAN + "You Got A Score Of:", score, "/", total_questions())

    if score >= passing_score:
        print(Fore.GREEN + "Congratulations! You have passed the driver's test!")
    else:
        print(Fore.RED + "Unfortunately, you did not pass the driver's test.")
        print(Fore.BLUE + "Here are the questions you answered incorrectly:")
        for i, question in enumerate(incorrect_answers):
            print(Fore.YELLOW + f"\nQuestion {i+1}:")
            print(question['question'])
            print("Correct Answer:", question['answer'])

        additional_correct_needed = passing_score - score
        print(Fore.BLUE + f"You need to answer {additional_correct_needed} more questions correctly to pass the LetsDrive test.")

# Runs the test
shuffle_questions()
run_driver_test()

