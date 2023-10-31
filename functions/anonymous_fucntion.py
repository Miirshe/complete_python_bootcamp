import lists_module as list_numbers
numbers = list_numbers.numbers
odd_number = lambda numbers : 'odd number' if numbers % 2 != 0 else 'even number'
print(f'the odd number : {odd_number(numbers)}')