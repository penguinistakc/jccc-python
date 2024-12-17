#!/usr/bin/env python3

"""
Write a program that asks the user to input two numbers.
The program should output the sum of the integers between
those two numbers.
• For example, if the user inputs the numbers 10 and 15, then
the sum would be 75.
10 + 11 + 12 + 13 + 14 + 15 = 75
"""

# Ask user for two numbers
start_num = int(input("Enter the first number: "))
end_num = int(input("Enter the second number: "))


# Ensure start is less than or equal to end for proper range calculation
if start_num > end_num:
    start_num, end_num = end_num, start_num

# Calculate the sum of integers between the two numbers (inclusive)
sum_of_nums = sum(range(start_num, end_num+1))

# Print the sum of the integers between the two numbers
print(f"The sum of integers between {start_num} and {end_num} is {sum_of_nums}")
