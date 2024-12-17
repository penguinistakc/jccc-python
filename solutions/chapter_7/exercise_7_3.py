#!/usr/bin/env python3

"""
Write a program that uses a loop to prompt the user and
get an integer value.
The program should print the sum of all the integers entered.
• If the user enters a blank line or any other line that cannot be
converted to an integer, the program should handle this
ValueError.
• If the user uses Ctrl-C to terminate the program, it should be
trapped with a KeyboadInterrupt, and a suitable
message should be printed.
• When the user enters the end of file character (Ctrl-D on
Linux or Ctrl-Z on Windows), the program should trap this
with the EOFError and break out of the loop and print the
sum of all the integers.
"""


def main():
    total_sum = 0
    print(
        "Enter integers to sum them up. Press Ctrl-D (Linux/Mac) or Ctrl-Z (Windows) to end."
    )

    while True:
        try:
            # Prompt the user for an integer input
            user_input = input("Enter an integer: ")

            # Try to convert the input to an integer
            number = int(user_input)
            total_sum += number

        except ValueError:
            # Handle non-integer inputs
            print("Invalid input. Please enter a valid integer.")

        except KeyboardInterrupt:
            # Handle Ctrl-C gracefully
            print("\nProgram interrupted with Ctrl-C. Exiting...")
            break

        except EOFError:
            # Handle end-of-file character (Ctrl-D or Ctrl-Z)
            print("\nEnd of input detected.")
            break

    # Print the total sum of all entered integers
    print(f"The total sum of entered integers is: {total_sum}")


if __name__ == "__main__":
    main()
