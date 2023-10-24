# Exercise 1
# The target of this exercise is to create a string, an integer,
# and a floating point number. The string should be named mystring and
# should contain the word "hello". The floating point number should be named myfloat
# and should contain the number 10.0, and the integer should be named myint and
# should contain the number 20.
# change this code
# ===========================================================

# mystring  = "hello"
# myfloat = 10.0
# myint = 20
# if mystring == "hello":
#     print('String:',mystring)
# if isinstance(myfloat , float) and myfloat == 10.0 :
#     print('Float:',myfloat)
# if isinstance(myint , int) and myint == 20 :
#     print('Integer:',myint)

# exercise 2
# create variable of string and put values of "hi miirshe", and then replace "hi" to "hello"
# ==============================================================

# greeting = "hi miirshe"
# if "hi" in greeting :
#     print(f'{greeting.replace("hi","hello")}')
# else:
#     print(f"OPPS 404 Not Found !")

# exercise 3
# create variable of String and put values of "hello miirshe" and then make all values as uppercase values
# ================================================================

# greeting = "hello miirshe"
# if greeting.islower():
#     print(f'{greeting.upper()}')
# else:
#     print(f'{greeting.lower()}')


# exercise 4 : Determine the Discount
# Write a Python program that asks the user for the original price of a product
# and their membership status. The program should calculate and display the final price after
# applying the discount based on the following rules:
#
#     If the user is a member (membership_status = True), apply a 10% discount.
#     If the user is not a member (membership_status = False), apply a 5% discount.

# def discount() :
#     try:
#         original_price = float(input('Enter Original Price ? : '))
#         member_status = input('Are you a member? (yes/no) : ')
#         if member_status != "yes" and member_status != "no":
#             print(f"you have only two options (yes/no) !", member_status)
#         elif member_status == 'yes':
#             print(f"Final price after discount: {original_price-(original_price * 0.10)}")
#         else:
#             print(f"Final price after discount: {original_price - (original_price * 0.05)}")
#     except Exception as exec:
#         print(exec)
#     finally:
#         print('your welcome feel free')
#
#
# discount()

# Assignment: Grade Calculator
#
# Write a Python program that prompts the user to enter the scores for four subjects:
#     Mathematics, English, Science, and History. The program should
#     calculate and display the average score as well as the corresponding grade based on the
#     following grading scale:

# def grade_calculator():
#
#     try:
#         total = 0.0
#         subjects = int(input('how many subjects to calculate ? : '))
#         i = 1
#         while i <= subjects:
#             marks = float(input(f'Enter a subject mark {i} ? :'))
#             total += marks
#             i += 1
#         average = total/subjects
#         if average >= 90 :
#             print(f'Your Grade : A \nYour Average : {average}')
#         elif average >= 80 :
#             print(f'Your Grade : B \nYour Average : {average}')
#         elif average >= 70 :
#             print(f'Your Grade : C \nYour Average : {average}')
#         elif average >= 60 :
#             print(f'Your Grade : D \nYour Average : {average}')
#         elif average < 60 :
#             print(f'Your Grade : F \nYour Average : {average}')
#     except Exception as exec:
#         print(exec)
#     finally:
#         print('feel free!')
#
#
# grade_calculator()


# THE PRACTICAL SESSION: Develop the following applications in Python using PyCharm,
# correct any sytax error, and share the results with your teacher.
# (1)	Ali, a Tutuk driver, would like to manage his income. Create a Python application that asks Ali
# for the total income and daily expenses, subtracts the expenses from the income, displays the net income,
# # and finally prints "Thank you for using this application."
# def manage_income():
#     total_income = float(input('Enter the total income ? : '))
#     daily_expenses = float(input('Enter daily expense ? : '))
#     income = total_income - daily_expenses
#     print(f'Net Income : {income}\nThank you for using this application.')
#
#
# manage_income()


# (2)	A company pays its employees based on their work hours with an hourly rate of 0.5 dollars per hour.
# Create a Python program that asks the user for the number of hours worked by the employee,
# multiplies worked hours by 0.5, and displays the amount every employee should receive.
# def calculate_hours_work():
#     user_hours = float(input('Enter work hours ? : '))
#     rate = 0.5
#     amount = user_hours*rate
#     print(f'You amount : ${amount} \nenjoy feel free')
#
#
# calculate_hours_work()

# (3)	Your Python teacher asks you to help him calculate the total marks for the class.
# Develop a Python program that asks the user for the subject marks and the assignment marks,
# then calculates the student's total marks and congratulates them for the achievement.
def calculate_subject_marks():
    subject_marks = float(input('Enter a subject marks ? : '))
    assignment_marks = float(input('Enter assignment marks : ? '))
    total_marks = subject_marks + assignment_marks
    print(f'The total marks : {total_marks}')


calculate_subject_marks()


