#!/usr/bin/env python3


def square(p):
    return p * p


def cube(p):
    return p * p * p


print("Module name is: " + __name__)


if __name__ == "__main__":
    print("Testing my functions at top level")
    print(square(5))
    print(cube(10))
