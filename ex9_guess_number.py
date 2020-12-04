#!/usr/bin/env python3

#Generate a random number between 1 and 9 (including 1 and 10). Ask the user to guess the number, 
# then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

random_number = random.randint(1, 11)
print(random_number)

user_guess = 0
user_attempt = 0

print("\nHello! I am thinking of a number between 1 and 10.")

while user_guess != "exit" or int(user_guess) != random_number:
    if user_attempt == 0:
        user_guess = input("Can you guess what it is (type exit to quit)? ")
    else:
        user_guess = input("\nTry again: ")
    if user_guess == "exit":
        print("Thanks for playing!")
    elif int(user_guess) == random_number:
        user_attempt+=1
        print(f"Wow, you are right the number is {random_number} and you guessed it in {user_attempt}!\n")
        break
    elif int(user_guess) > random_number:
        user_attempt+=1
        print(f"Sorry, {user_guess} is too high!")
    elif int(user_guess) < random_number:
        user_attempt+=1
        print(f"Sorry, {user_guess} is too low!")
    
  

