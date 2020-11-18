#!/usr/bin/env python3

# ask for a number
# print out if the number is odd or even
# Bonus1: If the number is divisable by 4 print out a different message
# Bonus2: Ask for 2 numbers and test to see if they are evenly divisable

user_number = input("Hello, enter a number and I will tell you if it is even or odd: ")
if int(user_number)%4 == 0:
    print(f"Wow, you chose {user_number} and it is divisable by 4!")
elif int(user_number)%2 == 0:
    print(f"The number {user_number} is even!")
else:
    print(f"The number {user_number} is odd, just like you!")