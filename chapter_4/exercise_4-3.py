#!/usr/bin/env python3

"""
Use a dictionary to create a mapping from the digits 0-9
to the words 'zero', 'one,' 'two,' etc.
Then, ask the user to input a number.
If the user enters 1437, then the program should print "one
four three seven."
"""

# Create a dictionary to map digits to words
digit_to_word = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

# Ask the user to input a number
user_input = input("Enter a number: ")

# Initialize an empty list to store the word representation of each digit
word_list = []

# Loop through each character in the user input
for digit in user_input:
    if digit in digit_to_word:
        word_list.append(digit_to_word[digit])

# Join the list into a string and print the result
print(" ".join(word_list))