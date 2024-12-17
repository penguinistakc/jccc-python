#!/usr/bin/env python3

import re

while True:
    line = input("Enter a string: ")
    if line == "q":
        break
    x = re.search("[0-9][0-9][0-9]", line)
    if x:
        print("3 consecutive digits found")
