# This program gives the user a simple math quiz
# two random numbers are generated and user prompted to input the result.
# If result is correct, user gets 1 point

# To do
# 1. Add options: for the answer
#   -get a random number and a random operator to modify the right answer
#   -just as you did the operator, get options A to D and assign the random answers to the random options
#   -you can do it.
# 2. create a file, Quiz.txt
#   - at the start of the quiz, get the UserName
#   - if username exists, append the latest quiz to the record of the user.
#   - if username does not exist, create the user profile
#       - Name:
#       - Time the test was taken(If possible, lol)
#       - Total Questions taken
#       - Total number of Correct Questions
#       - Total number of wrong questions
#       - Display percentage.
#       - Sum up user's total percentages, add the new percentage and display average percentage
# 3. Create another python program that will run the file for the user
# .
import random


def main():
    try:
        cont = ''
        stop = 's'
        correct = 0
        wrong = 0
        question_no = 1
        get_user_name()
        intro_message()  # display introduction message for user.

        try:
            level = int(input("Enter Level [1 - 4]: "))
            while level < 1 or level > 4:
                print('You entered a wrong value.'
                      'Enter a value between 1 and 4\n')
                level = int(input("Enter Level [1 - 4]: "))
        except ValueError:
            print("Try Again and Enter a value between 1 and 4\n")
        while (cont == 'q' or cont == '') and stop != '':
            num1 = choose_level(level)  # get random number from chooseLevel function, based on the level passed.
            num2 = choose_level(level)  # get random number from chooseLevel function, based on the level passed.

            if num1 == 0 or num2 == 0:
                break
            cont = 1

            print(f'  \nQuestion {question_no}')
            question_no += 1
            operator = random.randint(1, 5)      # 1 (+), 2 (*), 3 (-), 4 (/), 5 (%)
            if operator == 1:   # if operator is 1, give addition
                if num1 < num2:
                    print(f' {num2:^4}\n'
                          f'+{num1:^4}')
                    result = num1 + num2
                    answer = int(input("= "))
                else:
                    print(f'  {num1:^4}\n'
                          f'+ {num2:^4}')
                    result = num1 + num2
                    answer = int(input("= "))

                if answer == result:
                    print(f"Correct \\0/\n"
                          f"CONGRATULATIONS!!!")
                    correct += 1
                else:
                    print(f'Wrong :(\n'
                          f'{result} is the correct answer')
                    wrong += 1
                cont = input("Press 'Enter' to continue or 'q' to stop")
                if cont == 'q':
                    display_result(correct, wrong)
                    stop = input("Press 'Enter' to quit")

            elif operator == 2:     # if operator is 2, give multiplication
                if num1 < num2:
                    print(f'  {num2:^4}\n'
                          f'* {num1:^4}')
                    result = num1 * num2
                    answer = int(input("= "))
                else:
                    print(f'  {num1:^4}\n'
                          f'* {num2:^4}')
                    result = num1 * num2
                    answer = int(input("= "))

                if answer == result:
                    print(f"Correct \\0/\n"
                          f"CONGRATULATIONS!!!")
                    correct += 1
                else:
                    print(f'Wrong :(\n'
                          f'{result} is the correct answer')
                    wrong += 1
                cont = input("Press 'Enter' to continue or 'q' to stop ")
                if cont == 'q':
                    display_result(correct, wrong)
                    stop = input("Press 'Enter' to quit")

            elif operator == 3:     # if operator is 3, give subtraction
                print(f'  {num1:^4}\n'
                      f'- {num2:^4}')
                result = num1 - num2
                answer = int(input("= "))

                if answer == result:
                    print(f"Correct \\0/\n"
                          f"CONGRATULATIONS!!!")
                    correct += 1
                else:
                    print(f'Wrong :(\n'
                          f'{result} is the correct answer')
                    wrong += 1
                cont = input("Press 'Enter' to continue or 'q' to stop ")
                if cont == 'q':
                    display_result(correct, wrong)
                    stop = input("Press 'Enter' to quit")
            elif operator == 4:     # if operator is 4, give division
                print(f'  {num1} // {num2}')
                result = num1 // num2
                answer = int(input("= "))

                if answer == result:
                    print(f"Correct \\0/\n"
                          f"CONGRATULATIONS!!!")
                    correct += 1
                else:
                    print(f'Wrong :(\n'
                          f'{result} is the correct answer')
                    wrong += 1
                cont = input("Press 'Enter' to continue or 'q' to stop ")
                if cont == 'q':
                    display_result(correct, wrong)
                    stop = input("Press 'Enter' to quit")

            elif operator == 5:     # if operator is 5, give modulo.
                print(f'  {num1} % {num2}')
                result = num1 % num2
                answer = int(input("= "))

                if answer == result:
                    print(f"Correct \\0/\n"
                          f"CONGRATULATIONS!!!")
                    correct += 1
                else:
                    print(f'Wrong :(\n'
                          f'{result} is the correct answer')
                    wrong += 1
                cont = input("Press 'Enter' to continue or 'q' to stop ")
                if cont == 'q':
                    display_result(correct, wrong)
                    stop = input("Press 'Enter' to quit")
    except Exception as err:
        print(err)


def choose_level(level):
    if level == 1:  # Level 1
        num = random.randint(1, 10)
    elif level == 2:  # Level 2
        num = random.randint(10, 100)
    elif level == 3:  # Level 3
        num = random.randint(100, 1000)
    elif level == 4:  # Level 4
        num = random.randint(1, 1000)
    else:
        print("You entered a wrong level.")
        num = 0     # Sentinel
    return num


def get_user_name():
    pass
    # get username
    # ask if user is new or existing.


def intro_message():
    print(f'\nMATHS QUIZ \\O/\n'
          f'\nWelcome to this Simple Math Game.\n'
          f'You are allowed to choose a level between 1 to 4.\n'
          f'Level 1 being the simplest, Level 4 being the hardest\n'
          f'Be sure to enter a valid input\n'
          f'HELP:\n'
          f"'+' means addition\n"
          f"'-' means subtraction\n"
          f"'//' means integer division\n"
          f"'*' means multiplication\n"
          f"'%' means modulo or remainder division\n"
          f"Goodluck!\n")


def display_result(correct, wrong):
    percentage = (correct / (correct + wrong)) * 100
    print(f'You got {correct} questions correctly')
    print(f'You got {wrong} questions wrong')
    print(f'Your percentage is {percentage:.0f}%')


main()