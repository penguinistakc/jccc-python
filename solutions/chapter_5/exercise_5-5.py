#!/usr/bin/env python3

"""In Python, if you wish to reverse sort a list, you will need
to do the following.
values = [10, 40, 30, 20, 5]
values.sort()
values.reverse()
print(values)
Write your own versions of sort and reverse so that each of
the following is possible.
values = [10,40,30,20,5]
print(sort(values))
print(reverse(values))
print(reverse(sort(values)))
Make sure the lists themselves are not altered.
"""

def sort(values):
    # Return a new sorted list without modifying the original
    return sorted(values)

def reverse(values):
    # Return a new reversed list without modifying the original
    return list(reversed(values))

if __name__ == "__main__":
    # test the functions
    test_values = [10, 40, 30, 20, 5]
    # sort values and print result
    print(sort(test_values))
    # reverse the values and print result
    print(reverse(test_values))
    # sort the values, then reverse the sorted list and print the result
    print(reverse(sort(test_values)))