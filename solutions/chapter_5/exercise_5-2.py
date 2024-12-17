#!/usr/bin/env python3

"""
Write a function that is passed a variable number of
arguments and a number, say num, as its two
parameters.
The function should return the count of the values in the tuple
(the variable number of parameters) that are greater than num.
For example, one such call to the function is shown below.
res = pos(5, -10, 10, -20, 30, num=0)
In this case, the function would return 3.
"""


def greater_than_num(*args, num):
    # Initialize a counter for elements greater than num
    count = 0

    # Iterate through each element in args
    for value in args:
        # Check if the value is greater than num
        if value > num:
            count += 1

    # Return the count of values greater than num
    return count


if __name__ == "__main__":
    # Test the function
    result = greater_than_num(5, -10, 10, -20, 30, num=0)
    print(result)
