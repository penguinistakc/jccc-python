#!/usr/bin/env python3

import exercise_6_1a as ex1a


def my_first_function():
    print("First Function From This File")
    return "this is another function"


def a_function_to_prove_a_point():
    print("A Function To Prove A Point")
    return "This is a function to prove a point."


if __name__ == "__main__":
    ex1a.my_first_function()
    my_first_function()
    a_function_to_prove_a_point()
    ex1a.my_second_function()
