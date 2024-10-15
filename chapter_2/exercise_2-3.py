#!/usr/bin/env python3

"""
Write a program that prompts the user for a string and a number on separate lines.
The program should print the string replicated by the number.
- For example, if the string is "hello" and the number is 3, then 'hellohellohello' should be printed.
"""

# Ask the user for a string
user_string = input("Please enter a string: ")

# Ask the user for a number
user_number = input("Please enter a number: ")

# Convert the number to an integer
user_number_int = int(user_number)

# Print the string replicated by the number
print(user_string * user_number_int)