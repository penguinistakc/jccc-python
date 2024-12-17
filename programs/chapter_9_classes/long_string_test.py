#!/usr/bin/env python3

from operator import length_hint
from long_string_error import LongStringError

max_length = 10


def checkstring(s):
    length = len(s)
    if length > max_length:
        raise LongStringError("String too long", length)


while True:
    try:
        line = input("Enter a string: ")
        checkstring(line)
        print("line is OK")
    except LongStringError as e:
        print(e, e.length())
