#*******************MINI PROJECT ON QUIZ GAME IN PYTHON**************************** 
#***********developed by- VAMSI KRISHNA DESINEEDI(1602-21-748-059)*****************
# FUNCTION FOR NEW GAME
def new_game():
    guesses = [];correct_guesses = 0;question_num = 1;
    print("***********************Welcome to DVK QUIZ GAME*******************************")
    for key in questions:
        print("******************************************************************************")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Choose one option (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += checking_answer(questions.get(key), guess)
        question_num += 1
    show_score(correct_guesses, guesses)
# FUNCTION FOR CHECCKING THE ANSWER
def checking_answer(answer, guess):
    if answer == guess:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CORRECT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");print()
        return 1
    else:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WRONG<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");print()
        return 0
# FUNCTION FOR DISPLAYING THE SCORE
def show_score(correct_guesses, guesses):
    print("******************************************************************************")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!RESULTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("******************************************************************************")
    print("Correct Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Your Answers: ", end="")
    for i in guesses:
        print(i, end=" ")
    print();print()
    score = int((correct_guesses/len(questions))*100)
    print("Your SCORE : "+str(score)+"%");print()
# FUNCTION FOR PALYING AGAIN
def play_again():
    response = input("DO YOU WANT TO PLAY A NEW GAME? (YES or NO): ");print()
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
questions = {"Which of the following concepts is not a part of Python?: ": "A",
 "Which of the following statements are used in Exception Handling in Python?: ": "D",
 "How is a code block indicated in Python?: ": "B",
 "What is the maximum length of a Python identifier?: ": "D",
 "Which of the following types of loops are not supported in Python?: ": "C"}
options = [["A. Pointers", "B. Loops", "C. Dictionaries", "D. All of the Above"],
          ["A. try", "B. except", "C. finally", "D. All of the Above "],
          ["A. Brackets", "B. Indentation", "C. Key", "D. None of the Above"],
          ["A. 32", "B. 16", "C. 128", "D. No fixed length is specified"],
          ["A. for", "B. while", "C. do-while", "D. None of the Above "]]
new_game()
while play_again():
    new_game()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^COME BACK SOON^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


