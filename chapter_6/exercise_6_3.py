#!/usr/bin/env python3

"""
Write a Python program that sorts its command line arguments.
"""

import sys


def main():
    # Exclude the script name from the arguments
    args = sys.argv[1:]

    # Check if there are arguments to sort
    if not args:
        print("No arguments provided to sort.")
        return

    # Sort the arguments
    sorted_args = sorted(args)

    # Print the sorted arguments
    print("Sorted arguments:")
    for arg in sorted_args:
        print(arg)


if __name__ == "__main__":
    main()
