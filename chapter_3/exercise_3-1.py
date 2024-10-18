#!/usr/bin/env python3

"""
Write a program that prompts the user to enter two
integers, each on a separate line.
The program should print the larger of the two numbers.
"""

# Ask user for two numbers
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

# Check if num_1 is greater than num_2
if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_1 < num_2:
    print(f"{num_2} is greater than {num_1}")
else:
    print(f"{num_1} and {num_2} are equal")