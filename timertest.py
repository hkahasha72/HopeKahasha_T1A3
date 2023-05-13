import time


def timer_callback():
    # Implement the logic to be executed when the timer expires
    print("TIMES UP!!")

    # Create a Timer object that will call the timer_callback function after 25 minutes
    timer = threading.Timer(7, timer_callback)  

    # Start the timer
    timer.start()

    # Do other tasks here while the timer is running

print("Welcome to LetsDrive! the VIC Drivers Learner Test Practice app!, Input your name to start")
my_name = input()
print('Hello, ' + my_name + ' today youll be taking a practice drivers test which will help you prepare for the real thing, you will have 25 minutes to complete this test and must answer at least 26 out of the 32 questions correctly ')
print("Let's begin!\n")