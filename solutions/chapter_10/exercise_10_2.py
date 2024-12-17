import re

"""Repeat Exercise 1, but this time use a floating point
number.
A floating point number should have at least one digit to the left
and to the right of the decimal point.
Specify whether the number is positive or negative."""


def check_floating_point(line):
    """
    Check if the input line consists solely of a valid floating-point number
    and determine its sign (positive or negative).
    """
    # Regular expression for a valid floating-point number
    pattern = r"^-?\d+\.\d+$"

    # Check if the line matches the pattern
    if re.match(pattern, line.strip()):
        number = float(line.strip())
        if number > 0:
            return "The input is a positive floating-point number."
        elif number < 0:
            return "The input is a negative floating-point number."
        else:
            return "The input is zero (neither positive nor negative)."
    else:
        return "Invalid input. Please enter a valid floating-point number."


def main():
    print("Enter a line of input (type 'quit' to exit):")
    while True:
        # Read input from the user
        line = input("Enter a floating-point number: ")
        if line.lower() == "quit":
            print("Exiting the program. Goodbye!")
            break

        # Check and print the result
        result = check_floating_point(line)
        print(result)


if __name__ == "__main__":
    main()
