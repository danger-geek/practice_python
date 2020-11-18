#!/usr/bin/env python3

# ask for a number
# print out if the number is odd or even
# Bonus1: If the number is divisable by 4 print out a different message
# Bonus2: Ask for 2 numbers and test to see if they are evenly divisable

print("")
print("Hello, enter a number and a divisor and I will tell you if the number is evenly divided by the divisor!")
user_number = input("Enter a number: ")
user_divisor = input("Enter a divisor: ")
print("")
if int(user_number)%int(user_divisor) == 0:
    print(f"Wow, {user_number} is evenly divisable by {user_divisor}, you are amazing!")
else:
    print(f"Whomp whomp, {user_number} is NOT evenly divisable by {user_divisor}, better luck next time!")
print("")
