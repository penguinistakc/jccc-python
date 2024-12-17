#!/usr/bin/env python3

"""
Write a program that asks the user to input a number.
Repeat this process until the user enters the value "end."
Enter each number into a set.
However, before you enter the number, check to see if the
number is in the set.
Just before the program ends, print the set and the number of
elements that were NOT added to the set.
"""

# Initialize an empty set to store unique numbers
unique_numbers = set()

# Counter to keep track of numbers that were not added because they were duplicates
duplicate_count = 0

# Start a loop to get input from the user
while True:
    # Ask the user to input a number or "end" to stop
    user_input = input("Enter a number (or type 'end' to finish): ")

    # Check if the user wants to end the process
    if user_input.lower() == "end":
        break

    # Convert the input to an integer
    # try / except has not been discussed yet, but adding it here to illustrate how to test a value to be converted
    # and how to respond if the value is not a valid number
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Check if the number is already in the set
    if number in unique_numbers:
        print(f"{number} is already in the set. It won't be added again.")
        duplicate_count += 1  # Increment the count for duplicates
    else:
        unique_numbers.add(number)  # Add the number to the set

# Print the set of unique numbers
print("\nUnique numbers entered:", unique_numbers)

# Print the number of elements that were not added because they were duplicates
print(f"Number of duplicates that were not added: {duplicate_count}")