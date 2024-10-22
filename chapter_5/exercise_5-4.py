#!/usr/bin/env python3

"""
Re-write your solution to Exercise 5-3 using a lambda
function.
"""

def create_sum_function(a, b):
    # Return a lambda function that computes the sum of a and b
    return lambda: a + b

if __name__ == "__main__":
    # Test the function
    returned_function = create_sum_function(5, 10)

    # Execute the lambda function and print the result
    result = returned_function()
    print(result)