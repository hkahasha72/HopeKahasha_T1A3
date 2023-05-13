import random
import time
from colorama import init, Fore, Style
import json as json

# Initialize colorama
init(autoreset=True)

# This Section is the Defined, questions + answers for the driver's test, plus the hints
data_string = ''
{
    "questions": [
        {
            "question": "You are in a crash. The police are not in attendance. Someone is injured. What should you do?",
            "options": ["A: Make sure the injured person is alright then drive on", "B: Report the crash to the nearest open police station", "C: Report the crash to the nearest open police station if property has also been damaged"],
            "answer": "B",
            "hint": "it requires immediate action"
        },
        {
            "question": "What should you do when a worker on the road in front of you is holding a yellow circular sign that displays the text Slowly sign?",
            "options": ["A: Proceed slowly", "B: Proceed at the speed limit", "C: Stop and wait until it is safe to proceed slowly"],
            "answer": "A",
            "hint": "Its implied on the sign"
        },
        {
            "question": "When is vehicle A allowed to turn right?",
            "options": ["A: Before vehicle B turns right", "B: After vehicle B has turned right", "C: Vehicle A is not allowed to turn right."],
            "answer": "C",
            "hint": "Using a hands-free system allows you to communicate safely while driving."
        }
    ]
}
''
data = json.loads(question_string)

print(type(data))
print(data)


#Defines 
def display_question(question):
    print(Fore.YELLOW + question['question'])
    print(Fore.BLUE + "Hint:", question['hint'])
    for index, option in enumerate(question['options']):
        print(Fore.CYAN + f"{index + 1}. {option}")
    print(Style.RESET_ALL)

# defines 
def run_driver_test():
    score = 0
    total_questions = len(questions)
    incorrect_answers = []


    print(Fore.GREEN + "Welcome to LetsDrive! the VIC Drivers Learner Test Practice app!, Input your name to start")
    my_name = input()
    print('Hello, ' + my_name + ' today youll be taking a practice drivers test which will help you prepare for the real thing, you will have 25 minutes to complete this test and must answer at least 26 out of the 32 questions correctly ')
    print("Let's begin!\n")

    # Gives reader time to read the description before the test starts
    time.sleep(7)

    # Shuffle the questions
    random.shuffle(questions)

    # Iterate through the questions
    for question in questions:
        display_question(question) 
        user_answer = input(Fore.WHITE + "Enter answer A, B, C: ").strip().upper()
       

        # Check the answer
        if user_answer == question['answer'].upper():
            score += 1
            print(Fore.GREEN + "Correct!")
        else:
            incorrect_answers.append(question)
            print(Fore.RED + "Incorrect!")
           

        print()

    # Calculate the passing score
    passing_score = int(0.8 * total_questions)

    print(Fore.BLUE + "Test complete " + my_name + "!")
    print(Fore.CYAN + "You Got A Score Of:", score, "/", total_questions)

    if score >= passing_score:
        print(Fore.GREEN + "Congratulations! You have passed the driver's test!")
    else:
        print(Fore.RED + "Unfortunately, you did not pass the driver's test.")
        print(Fore.BLUE + "Here are the questions you answered incorrectly:")
        for i, question in enumerate(incorrect_answers):
            print(Fore.YELLOW + f"\nQuestion {i+1}:")
            print(question['question'])
            print("Correct Answer:", question['answer'])

run_driver_test()