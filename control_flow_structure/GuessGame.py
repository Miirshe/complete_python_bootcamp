# Challenge 5: Guessing Game
# Write a program that generates a random number between 1 and 100.
# Prompt the user to guess the number and provide feedback
# if the guess is too high or too low. Repeat the process until
# the user guesses the correct number.
import random


def gussingGame(number):

    r_number = random.randint(1,100)
    if number > 100:
        print(f'{number} between 1 and 100 no more ! ')
    elif r_number == number:
        print(f'draw : {r_number} and {number}')
    elif r_number > number:
        result = r_number - number
        if result > 10:
            print(f'too high {result}')
        else:
            print(f'high {result} ')
    elif r_number < number:
        result = number - r_number
        if result > 10:
            print(f'too low {result} ')
        else:
            print(f'low {result} => {r_number} {number}')
    else:
        print('invalid number')


gussingGame(40)

