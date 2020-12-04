#!/usr/bin/env python3

#Generate a random number between 1 and 9 (including 1 and 10). Ask the user to guess the number, 
# then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

random_number = random.randint(1, 11)
print(random_number)

user_guess = int(input("\nHello! I am thinking of a number between 1 and 10, can you guess what it is? "))

if user_guess == random_number:
    print(f"Wow, you are right the number is {random_number}!")
elif user_guess > random_number:
    print(f"Sorry, {user_guess} is too high!")
elif user_guess < random_number:
    print(f"Sorry, {user_guess} is too low!")    

