import re

"""Write a program that reads a line at a time and
determines whether the input consists solely of an integer
number that is positive or negative.
Specify whether it is positive or negative.
"""


def check_integer(line):
    """
    Check if the input line consists solely of an integer and determine its sign.
    """
    # Regular expression to match a positive or negative integer
    pattern = r"^-?\d+$"

    # Check if the line matches the pattern
    if re.match(pattern, line.strip()):
        number = int(line.strip())
        if number > 0:
            return "The input is a positive integer."
        elif number < 0:
            return "The input is a negative integer."
        else:
            return "The input is zero (neither positive nor negative)."
    else:
        return "Invalid input. Please enter a valid integer."


def main():
    print("Enter a line of input (type 'quit' to exit):")
    while True:
        # Read input from the user
        line = input("Enter a number: ")
        if line.lower() == "quit":
            print("Exiting the program. Goodbye!")
            break

        # Check and print the result
        result = check_integer(line)
        print(result)


if __name__ == "__main__":
    main()
