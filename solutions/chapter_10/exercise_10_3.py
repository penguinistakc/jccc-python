"""Write a program that reads lines from the user one at a
time to see if they are formatted according to the following
criteria.
Correctly formatted lines should consist of a four character part
number, any number of spaces or tabs, and a description.
The four characters should consist of two digits and two
uppercase characters.
For each correctly formatted line, print the two digits, the two
characters, and the descriptions.
• Print all of these pieces of information on separate lines.
"""

import re


def main():
    print("Enter lines to check their format (type 'quit' to exit):")
    # Regular expression for the format: two digits, two uppercase letters, spaces/tabs, and a description
    pattern = r"^(\d{2})([A-Z]{2})[\s\t]+(.+)$"

    while True:
        # Read input from the user
        line = input("Enter a line: ").strip()

        if line.lower() == "quit":
            print("Exiting the program. Goodbye!")
            break

        # Match the line against the pattern
        match = re.match(pattern, line)
        if match:
            digits = match.group(1)  # First group: two digits
            letters = match.group(2)  # Second group: two uppercase letters
            description = match.group(3)  # Third group: description

            # Print the extracted components
            print("Correctly formatted line:")
            print(f"Two digits: {digits}")
            print(f"Two uppercase characters: {letters}")
            print(f"Description: {description}\n")
        else:
            print("Invalid format. Please enter a line in the correct format.\n")


if __name__ == "__main__":
    main()
