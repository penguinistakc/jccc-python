#!/usr/bin/env python3

import re

while True:
    line = input("Enter a string: ")
    if line == "q":
        break
    x = re.search("the", line)
    print(type(x))
    if x:
        print("'the' found")
    else:
        print("No match found")
