#!/usr/bin/env python3

import re

while True:
    line = input("Enter a string: ")
    if line == "q":
        break
    x = re.search("\+\*", line)
    if x:
        print("'+*' found")
