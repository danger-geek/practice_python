#!/usr/bin/env python3

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b_list = [element for element in a_list if element%2==0]
print(b_list)