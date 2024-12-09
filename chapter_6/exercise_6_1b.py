#!/usr/bin/env python3

import exercise_6_1a as ex1a


# Test the functions from the imported module
def yet_another_function():
    print("Yet Another Function")
    return "This is yet another function."


if __name__ == "__main__":
    ex1a.my_first_function()
    ex1a.my_second_function()
    ex1a.my_third_function()
    yet_another_function()
