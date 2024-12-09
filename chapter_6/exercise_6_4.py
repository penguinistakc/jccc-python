#!/usr/bin/env python3

"""
Write a program that sums the command line arguments.
"""

import sys


def main():
    # Exclude the script name from the arguments
    args = sys.argv[1:]

    # Check if there are arguments to sum
    if not args:
        print("No arguments provided to sum.")
        return

    try:
        # Convert arguments to numbers and calculate the sum
        total = sum(float(arg) for arg in args)
        print(f"The sum of the arguments is: {total}")
    except ValueError:
        print("Error: All command-line arguments must be numbers.")


if __name__ == "__main__":
    main()
