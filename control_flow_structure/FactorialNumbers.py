# Challenge 4: Factorial Calculator
# Write a program that calculates the factorial of a given number.
# Prompt the user to enter a number, and then display the factorial value.

def factorialNumbers(number):
    if number < 1:
        print(' enter more than 0 ')
    factorial = 1;
    i = number
    while i >= 1:
        factorial *= i
        i -= 1
    print(f'The Factorial Number of {number} : {factorial}')


factorialNumbers(5)

