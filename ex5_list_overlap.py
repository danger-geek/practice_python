#!/usr/bin/env python3

# write a program that returns a list that contains only the elements that are common between the lists (without duplicates) 
# Make sure your program works on two lists of different sizes.

# Bonus 1 Randomly generate two lists to test this
# Bonus 2 Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

#a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a_list = []
b_list = []

for item in range(0,10):
    n = random.randint(1,30)
    a_list.append(n)

for item in range(0,10):
    n = random.randint(1,30)
    b_list.append(n)

c_list = a_list + b_list
unique_list =[]

for item in c_list:
    if item not in unique_list:
        unique_list.append(item)

print(f"\na_list = {a_list}")
print(f"b_list = {b_list} ")
print(f"Sorted list with only unique numbers = {sorted(unique_list)}")
