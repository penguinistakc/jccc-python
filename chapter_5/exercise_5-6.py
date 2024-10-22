#!/usr/bin/env python3

"""
Write and test a function that takes two lists as arguments
and returns a list of the elements that are common to both
of the argument lists.
"""


def common_elements(list1, list2):
    # Create an empty list to store common elements
    common = []

    # Iterate through each element in the first list
    for element in list1:
        # Check if the element is also in the second list and not already in the common list
        if element in list2 and element not in common:
            common.append(element)

    return common


if __name__ == "__main__":
    # Test the function
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    result = common_elements(list1, list2)
    print(result)