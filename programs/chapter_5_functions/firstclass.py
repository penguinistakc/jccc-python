#!/usr/bin/env python3


def square(p):
    return p * p


def increment(p):
    return p + 1


def compute(func, lis):
    for index, item in enumerate(lis):
        lis[index] = func(item)


if __name__ == "__main__":
    print("Testing my functions at top level")
    print(square(5))
    print(increment(5))
    lis = [10, 20, 30, 40, 50]
    compute(square, lis)
    print(lis)
    compute(increment, lis)
    print(lis)
    print("End of test")
