num = int(input('Enter a factorial number ? : '))


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


factorial_number = factorial(num)
print(f'The factorial number {num} : {factorial_number}')


def sumNumber(num):
    if num == 1:
        return  1
    else:
        return num+sumNumber(num -1)


number = sumNumber(num)
print(f'The sum number : {number}')