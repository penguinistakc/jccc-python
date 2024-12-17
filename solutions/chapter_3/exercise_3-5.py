#!/usr/bin/env python3

"""
Produce a table of the integers from 0 to 49.
Try to get 10 items per row as shown below.
0 1 2 3 4 5 6 7 8 9
10 11 12 13 14 15 16 17 18 19
20 21 22 23 24 25 26 27 28 29
30 31 32 33 34 35 36 37 38 39
40 41 42 43 44 45 46 47 48 49
"""

# Loop through numbers from 0 to 49
for i in range(0, 50):
    # Print the number followed by a space, and add a newline after every 10 numbers
    print(i, end=" ")
    # Use the modulo operator to check if the number is a multiple of 10
    if (i + 1) % 10 == 0:
        print()  # Move to the next line after every 10 numbers