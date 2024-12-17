#!/usr/bin/env python3

"""
Write and test a function that takes a number and a
dictionary and adds the number to all values in the
dictionary.
You can assume that all the values (but not necessarily the
keys) in the dictionary are numbers.
"""


def add_to_values(number, input_dict):
    # Create a new dictionary to store the updated values
    updated_dict = {}

    # Iterate through each key-value pair in the input dictionary
    for key, value in input_dict.items():
        # Add the number to the current value and store it in the new dictionary
        updated_dict[key] = value + number

    return updated_dict


if __name__ == "__main__":
    # Test the function
    test_dict = {"a": 1, "b": 2, "c": 3}
    result = add_to_values(10, test_dict)
    print(result)