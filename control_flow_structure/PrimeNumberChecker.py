# Challenge 2: Prime Number Checker
# Write a program that checks if a given number is prime.
# Prompt the user to enter a number, and then display a message
# indicating whether the number is prime or not.
import math


def primeNumberCheck(number):
    if number < 2:
        print(f'{number} Not prime number ')
        return
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            print(f'{number} Not Prime number')
            return
        else:
            print(f'{number} Prime number')
            return
    i += 1


primeNumberCheck(4)
primeNumberCheck(5)
primeNumberCheck(10)


