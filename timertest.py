import time


def timer_callback():
    # Implement the logic to be executed when the timer expires
    print("TIMES UP!!")

    # Create a Timer object that will call the timer_callback function after 25 minutes
    timer = threading.Timer(7, timer_callback)  
    # 1500 seconds = 25 minutes

    # Start the timer
    timer.start()

    # Do other tasks here while the timer is running

