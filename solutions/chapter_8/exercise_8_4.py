#!/usr/bin/env python3

"""
Write a program that displays the file name, size, and
modification date for all those files in a directory that are
greater than a certain size.
The directory name and the size criteria are given as command
line arguments.
If the number of command line arguments is incorrect, the
program should print an error message and terminate.
"""

import os
import sys
from datetime import datetime


def main():
    # Check if the correct number of command-line arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python file_info.py <directory_name> <size_in_bytes>")
        sys.exit(1)
    # Get the directory name and size criteria from command-line arguments
    directory = sys.argv[1]
    try:
        size_criteria = int(sys.argv[2])
    except ValueError:
        print("Error: Size criteria must be an integer (size in bytes).")
        sys.exit(1)

    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)

    print(f"Files in '{directory}' larger than {size_criteria} bytes:\n")

    # Iterate over all files in the specified directory
    try:
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)

            # Check if it's a file (not a directory)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)  # Get file size
                if file_size > size_criteria:
                    mod_time = os.path.getmtime(file_path)  # Get modification time
                    mod_time_formatted = datetime.fromtimestamp(mod_time).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )

                    # Display file details
                    print(f"File: {file_name}")
                    print(f"Size: {file_size} bytes")
                    print(f"Last Modified: {mod_time_formatted}\n")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
