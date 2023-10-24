# def sum_2_arr():
#     arr1 = [1, 2, 3]
#     arr2 = [1, 2, 3]
#     arr3 = []
#     for num1 in arr1:
#         for num2 in arr2:
#             if num1 == num2:
#                 num = num1 + num2
#                 arr3.append(num)
#     print(f'The Numbers of arr1 : {arr1}')
#     print(f'The Numbers of arr2 : {arr2}')
#     print(f'Sum of arr1 and arr2 : {arr3}')
#
#
# sum_2_arr()
import random

# def sum_numbers():
#     nums = [1, 2, 3, 4, 5, 6]
#     sum = 0
#     for num in nums:
#         sum += num
#     print(f'The Sum Of Lists : {sum}')
#
# sum_numbers()


# # convert word into array of list
# def words_into_list(words):
#     letters = words.split(" ")
#     print(letters)
# words_into_list('hi miirshe how is your day')

# convert array of list into single word
# def lists_into_words():
#     words = ['hi', 'miirshe', 'how', 'is', 'your', 'day']
#     letters = " ".join(words)
#     print(letters)
# lists_into_words()

#copy exist of array lists
# def copy_array():
#     arr1 = ['miirshe',23,'male']
#     arr2 = arr1.copy()
#     print(f'The Copy Of Array List : {arr2}')
#
# copy_array()

# def length_array():
#     arr1 = ['miirshe', 23, 'male']
#     print(f'The Length of array : {len(arr1)}')
#
#
# length_array()
# task = input('Enter your task ? : ')
# id = random.randint(1,100)
# def addlists(values):
#     todo = [
#         {
#             "id" : 1,
#             "task" : "hard work"
#         }
#     ]
#     for task in todo:
#         if task["id"] != values["id"]:
#             todo.insert(values["id"],values)
#             print(f'todo : {todo}')
#         else:
#             print('Task already exist ! ')
#
# addlists({"id" : id ,"task" : task})


def updatelists(values):
    todo = [
        {
            "id" : 1,
            "task" : "hard work"
        }
    ]
    for task in todo:
        if task["id"] == values["id"]:
            task["task"] = values['task']
            # print(f'successfully clear: {todo.clear()}')
            print(f'successfully updated : {todo}')
        else:
            print('Task Not exist ! ')

updatelists({"id" : 1 ,"task" : 'excellent works '})