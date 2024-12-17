#!/usr/bin/env python3

"""
Write a program that prompts for two numbers.
- The first number will be the base, and the second number will be the exponent.
- Print the result of raising the base (first number) to the power of the exponent (second number).
"""

# Ask the user for a value for the base
base = input("What is the base? ")

# Ask the user for a value for the exponent
exponent = input("What is the exponent? ")

# Convert the base to an integer
base_int = int(base)

# Convert the exponent to an integer
exponent_int = int(exponent)

# Calculate the result of raising the base to the power of the exponent
result = base_int ** exponent_int # alternate solution: result = pow(base_int, exponent_int)

# Print the result to the screen
print("The result of raising the base to the power of the exponent is: ", result)
