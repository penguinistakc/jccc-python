#!/usr/bin/env python3

"""
Write a program that accepts a string from the user.

Determine the following information about the string.
- Does it end in a period?
- Does it contain all aphabetic characters?
- Is there an 'x' in the string?

Use the len() function to determine the length of the string.
- Is the newline character (\n) part of the string?

Change all occurences of 'e' to 'E' in the string.
"""

# Ask the user for a string
user_string = input("Please enter a string: ")

# Determine if the string ends in a period
ends_in_period = user_string.endswith(".")

# Print if the string ends in a period
print("Does the string end in a period? ", ends_in_period)

# Determine if the string contains all alphabetic characters
is_alpha = user_string.isalpha()

# Print if the string contains all alphabetic characters
print("Does the string contain all alphabetic characters? ", is_alpha)

# Determine if there is an 'x' in the string
contains_x = "x" in user_string

# Print if there is an 'x' in the string
print("Is there an 'x' in the string? ", contains_x)

# Determine the length of the string
string_length = len(user_string)

# Print the length of the string
print("The length of the string is: ", string_length)

# Change all occurrences of 'e' to 'E' in the string
new_string = user_string.replace("e", "E")

# Print old string and new string
print("Old string: ", user_string)
print("New string: ", new_string)
