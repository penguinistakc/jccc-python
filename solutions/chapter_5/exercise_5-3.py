#!usr/bin/env python3

"""
Write a function that returns a function that, when
executed, returns the sum of two integers.
"""


def create_sum_function(a, b):
    # Define the inner function that returns the sum of a and b
    def sum_function():
        return a + b

    # Return the inner function
    return sum_function


if __name__ == "__main__":
    # test function
    returned_function = create_sum_function(5, 10)

    # Execute the inner function and print the result
    result = returned_function()
    print(result)