#!/usr/bin/env python3

# ask for a number
# print out if the number is odd or even

user_number = input("Hello, enter a number and I will tell you if it is even or odd: ")
if int(user_number)%2 == 0:
    print(f"The number {user_number} is even!")
else:
    print(f"The number {user_number} is odd, just like you!")