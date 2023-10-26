# Challenge 1: FizzBuzz
# Write a program that prints the numbers from 1 to 100.
# But for multiples of three, print "Fizz" instead of the number,
# and for multiples of five, print "Buzz". For numbers that are multiples of both
# three and five, print "FizzBuzz".

def fizzbuzz():
    for num in range(1, 100):
        if num % 3 == 0:
            print(f'Fizz     : {num}')
        elif num % 5 == 0:
            print(f'Buzz      : {num}')
        else:
            print(f'FizzBuzz  : {num}')


fizzbuzz()
