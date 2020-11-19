#!/usr/bin/env python3

# print out all the numbers from a list that are less than 10
# Bonus1 - create a new list and then print it
# Bonus2 - write in one line of python
# Bonus3 - ask user for a number then print all the numbers from the list that are less than the number

numbers_list = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]

print("Thanks for the list, the following numbers are less than 10:")
less_than_list = []
for number in numbers_list:
    if number < 10:
        less_than_list.append(number)
print(less_than_list)
