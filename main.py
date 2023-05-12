



# This Section is the Defined, questions + answers for the driver's test, plus the hints 
questions = [
    {
        'question': 'You are in a crash. The police are not in attendance. Someone is injured. What should you do?',
        'options': ['A: Make sure the injured person is alright then drive on', 'B: Report the crash to the nearest open police station', 'C: Report the crash to the nearest open police station if property has also been damaged'],
        'answer': 'B',
        'hint': 'it requires imediate action'
    },
    {
        'question': 'What should you do when a worker on the road in front of you is holding a yellow circular sign thta displays the text "Slowly" sign?',
        'options': ['A: Proceed slowly', 'B: Proceed at the speed limit', 'C: Stop and wait until it is safe to proceed slowly'],
        'answer': 'A',
        'hint': 'Its implied on the sign'
    },
    {
        'question': 'When is vehicle A allowed to turn right?',
        'options': ['A: Before vehicle B turns right', 'B: After vehicle B has turned right ','C: Vehicle A is not allowed to turn right.'],
        'answer': 'A',
        'hint': 'Using a hands-free system allows you to communicate safely while driving.'
    },
    
]


def run_driver_test():
    score = 0
    total_questions = len(questions)
    incorrect_answers = []

    print( "Welcome to LetsDrive! the VIC Drivers Learner Test Practice app!, Input your name to start")
    my_name = input()
    print('Hello, ' + my_name + ' today youll be taking a practice drivers test which will help you prepare for the real thing, you will have 25 minutes to complete this test and must answer at least 26 out of the 32 questions correctly ')
    print("Let's begin!\n")
    
   

    # Iterate through the questions
    for question in questions:
        print(question['question'])
        for option in question['options']:
            print(option)
        user_answer = input("Enter your answer as so A, B or C: ").strip().upper()

        # Check the answer
        if user_answer == question['answer'].upper():
            score += 1
        else:
            incorrect_answers.append(question)

        print()

    # Calculate the passing score
    passing_score = int(0.8 * total_questions)

    print("Test complete!")
    print("Score:", score, "/", total_questions)

    if score >= passing_score:
        print("Congratulations! You passed the driver's test!")
    else:
        print("Unfortunately, you did not pass the driver's test.")
        print("Here are the questions you answered incorrectly:")
        for i, question in enumerate(incorrect_answers):
            print(f"\nQuestion {i+1}:")
            print(question['question'])
            print("Correct Answer:", question['answer'])
            

run_driver_test()