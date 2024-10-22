#!/usr/bin/env python3

"""
Write a function that receives a list as its parameter and returns a new list of the positive
elements only.
"""


def get_positive_elements(input_list):
    # Initialize an empty list to store positive elements
    positive_elements = []

    # Iterate through each element in the input list
    for element in input_list:
        # Check if the element is positive
        if element > 0:
            positive_elements.append(element)

    # Return the list of positive elements
    return positive_elements

if __name__ == "__main__":
    # Test the function
    test_list = [1, -2, 3, -4, 5, -6, 7, -8, 9]
    result = get_positive_elements(test_list)
    print(result)