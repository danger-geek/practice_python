#!/usr/bin/env python3
# 
import datetime 

"""
Simple program to calculate the year the user will turn 100yo
"""
username = input("Hello, what is your name? ")
userage = input(f"Nice to meet you {username}, how old are you? ")
current_date = datetime.datetime.now()
current_year = current_date.year

when_100_yo = 100-int(userage)+current_year 

print(f"{username}, did you know you will turn 100 years old in {when_100_yo}!")