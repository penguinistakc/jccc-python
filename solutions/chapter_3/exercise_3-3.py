#!/usr/bin/env python3

"""
Ask the user to input a set of numbers on one input line.
Split the numbers into a list.
Write a loop that examines each element of the list and displays
the ones that are greater than zero.
"""

# Ask user for a set of numbers
user_input = input("Enter a set of numbers separated by spaces: ")

# Split the numbers into a list
num_list = user_input.split()

# Loop through the list and display numbers greater than zero
for num in num_list:
    # Convert to integer and test if it is greater than 0
    if int(num) > 0:
        # print the number if it is > 0
        print(num)