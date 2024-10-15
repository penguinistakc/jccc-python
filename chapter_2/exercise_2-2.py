#!/usr/bin/env python3

"""
Write a program that reads two integers, each on a separate line.
- Print the product of the two numbers
Once this works properly, try entering numbers with a decimal point
- What happens? Why?
Now try entering data that is non-numeric.
- What happens? Why?
"""

# Ask the user for a value for the first number
first_number = input("What is the first integer? ")

# Ask the user for a value for the second number
second_number = input("What is the second integer? ")

# Convert the first number to an integer
first_number_int = int(first_number)

# Convert the second number to an integer
second_number_int = int(second_number)

# Calculate the product of the two numbers
product = first_number_int * second_number_int

# Print the number to the screen
print("The product of the two numbers is: ", product)

