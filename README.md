# LetsDrive README.md

### Description:
LetsDrive is an interactive mobile application designed to help users practice for their driver's test. The app provides a simulated environment that resembles a legitimate driver's test, offering various features to enhance learning and track progress. It includes a built-in timer, feedback system, progress tracking, and personalized hints, LetsDrive ensures users feel confident and prepared for their real driver's test.

##### Link to your source control repository:


#### Code style guide or styling conventions that the application will adhere to:
colorama - init, Fore, Style


#### Features in app

###### Timer: 
LetsDrive includes a timer which mimic the time constraints of a real driver's test allowing them to improve their speed and time management skills.

###### Feedback and Progress:
After answering a question, the app provides instant feedback, allowing the use to know whether the chosen answer is correct or incorrect. If the user selects an incorrect answer, the user will be notifed and told the correct answer after the test for study purposes. Users can track their progress through a visual representation of their overall performance and review their scores for each session.

###### Scoring System: 
At the end of each practice session, LetsDrive displays the user's final score, iforming them of the number of correct answers. This information helps users see their performance and know the areas that require more improvement.

###### Passing Requirement: 
LetsDrive calculates the minimum number of correct answers needed in order to pass a driver's test in the user's VIC. After each practice session, the app lets the users know about how many more correct answers they need to achieve to meet the passing criteria.

###### Progress Tracking: 
LetsDrive maintains a user profile that stores performance history, allowing users to track their progress at the end which presents a comprehensive overview of past sessions, scores, and areas of improvement, enabling users to focus on weak points.

###### Feedback system:
Gives users feedback about how much more point they need in order to improve their score which would allow them to pass the amount of correct questions they need



#### Proof features above demonstrate my understanding of the following language elements and concepts:
- ###### Variables and Variable Scope:
These are shown through my use of `score` and `incorrect_answers` as they are variables which are used to store and track the users score and the list of the users incorrectly answered questions. The use of the `passing_score` is a variable which calculates the passing score based on the total amount of questions. Lastly another example is `my_name`, it is a variable that stores the users name which they inputed.

- ###### Loops:
The `for` loop repeats through each question in `test_question['test_question']`.

- ###### Conditional Control Structures:
Conditional control structures are shown through the `if-else` statement, it checks if the user's answer is correct or whether its incorrect, then it updates the score accordingly, `if-else` taht shows up again is a statement which checks if the user's score meets the passing score criteria and displays the appropriate message.

- ###### Error Handling:
The use of `try-except` block uses a form of error handling to take care of the `TimeoutOccurred` exception which is raised by `inputimeout`, If the user doesn't provide an answer (input) within the time specified, the code moves on to the next question and appends the current question to the `incorrect_answers` list.


#### Proof of approval from educator that features are sufficient


##### reference to an accessible project management platform used to track this implementation plan. 


> Your checklists for each feature should have at least 5 items.

R8	
#### help documentation which includes a set of instructions which accurately describe how to use and install the application.

You must include:
###### steps to install the application
###### dependencies required by the application to operate
###### any system/hardware requirements
###### how to use any command line arguments made for the application

# References
- Colorama install:  https://blog.finxter.com/how-to-install-colorama-in-python/  ,, https://www.youtube.com/watch?v=u51Zjlnui4Y 