#!/usr/bin/env python3

"""
Ask the user to input three numbers representing a lower
limit, a higher limit, and a step value.
The program should loop through and print the numbers from
low to high, taking into consideration the step.
A for loop and range function should be used for this
exercise.
"""

# Ask the user to input the lower limit, higher limit, and step value
low = int(input("Enter the lower limit: "))
high = int(input("Enter the higher limit: "))
step = int(input("Enter the step value: "))

# Loop through and print the numbers from low to high, considering the step
print(f"Numbers from {low} to {high} with a step of {step}:")
for num in range(low, high + 1, step):
    print(num)