#!/bin/bash

pip install colorama inputimeout 


import time
from colorama import init, Fore, Style
import json
from inputimeout import inputimeout, TimeoutOccurred
import random

init(autoreset=True)

with open('test_question.json') as f:
test_question = json.load(f)

def display_question(question):
print(Fore.YELLOW + question['question'])
print(Fore.BLUE + "Hint:", question['hint'])
for index, option in enumerate(question['options']):
print(Fore.CYAN + f"{index + 1}. {option}")
print(Style.RESET_ALL)

def total_questions():
return len(test_question['test_question'])


def shuffle_questions():
random.shuffle(test_question['test_question'])

def run_driver_test():
score = 0
incorrect_answers = []

echo "${Fore[GREEN]}Welcome to LetsDrive! the VIC Drivers Learner Test Practice app! Input your name to start"
read -r my_name
echo "Hello, $my_name today you'll be taking a practice driver's test which will help you prepare for the real thing. You will have 25 minutes to complete this test and must answer at least 26 out of the 32 questions correctly."
echo "Let's begin!"
    

sleep 3

shuffle_questions

for question in test_question['test_question']:
display_question(question)
read -r -t 7 -p "${Fore[WHITE]}Enter answer A, B, C: " user_answer || true
user_answer=$(echo "$user_answer" | awk '{print toupper($0)}')

if [[ $user_answer == "${question['answer']^^}" ]]; then
score=$((score + 1))
echo "${Fore[GREEN]}Correct!"
else
incorrect_answers+=("$question")
echo "${Fore[RED]}Incorrect!"
fi

echo ""

passing_score=$((total_questions * 8 / 10))

echo "${Fore[BLUE]}Test complete, $my_name!"
echo "${Fore[CYAN]}You Got A Score Of: $score / $total_questions"

if (( score >= passing_score )); then
echo "${Fore[GREEN]}Congratulations! You have passed the driver's test!"
else
echo "${Fore[RED]}Unfortunately, you did not pass the driver's test."
echo "${Fore[BLUE]}Here are the questions you answered incorrectly:"
for (( i = 0; i < ${#incorrect_answers[@]}; i++ )); do
echo "${Fore[YELLOW]}"
echo "Question $((i + 1)):"
echo "${incorrect_answers[$i]['question']}"
echo "Correct Answer: ${incorrect_answers[$i]['answer']}"
done

additional_correct_needed=$((passing_score - score))
echo "${Fore[BLUE]}You need to answer $additional_correct_needed more questions correctly to pass the LetsDrive test."
fi
done

shuffle_questions
run_driver_test
