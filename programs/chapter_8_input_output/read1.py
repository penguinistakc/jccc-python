#!/usr/bin/env python3

import sys

ct = lines = 0
with open(sys.argv[1], "r") as file:

    while True:
        line = file.readline()
        if not line:
            break
        ct += len(line)
        lines += 1

# file.close()
print("Characters: ", ct, " Lines: ", lines)
