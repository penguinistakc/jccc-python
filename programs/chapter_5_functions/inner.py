#!/usr/bin/env python3
def outer(a, b):
    x = 15
    y = 20

    def inner():
        print(a, b, x, y)

    return inner  # reference to inner function


y = outer(5, 10)
print(type(y))
y()  # prints 5 10 15 20
