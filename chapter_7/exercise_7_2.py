#!/usr/bin/env python3

"""
Create a list in your program that has 10 numbers.
Then, in a loop, ask the user for a number.
• Use this number as an index into your list and print the valuelocated at that index.
• End the program when the user enters "end."
• Handle the case of an illegal number.
• Handle the case of an illegal subscript.

Eliminate negative numbers as legitimate input by raising the IndexError exception.
"""


def main():
    # A list of ten numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    print("You can retrieve values from the list using an index (0-9).")
    print("Type 'end' to exit the program.")

    while True:
        # Prompt the user for a number or 'end'
        user_input = input("Enter an index (0-9) or 'end': ")

        # Check if the user wants to exit
        if user_input.lower() == "end":
            print("Exiting the program. Goodbye!")
            break

        # Validate and process the input
        # Eliminate negative numbers as legitimate input by raising the IndexError exception
        try:
            index = int(user_input)
            if 0 <= index < len(numbers):
                print(f"Value at index {index}: {numbers[index]}")
            elif index < 0:
                raise IndexError("Error: Negative index is not allowed.")
            else:
                print(
                    "Error: Index out of range. Please enter a number between 0 and 9."
                )
        except ValueError:
            print("Error: Invalid input. Please enter a valid number or 'end'.")


if __name__ == "__main__":
    main()
