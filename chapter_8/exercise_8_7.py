import sys

"""Write a program that counts the number of lines, words,
and characters in each file named on the command line.
"""


def count_file_statistics(file_name):
    """
    Count the number of lines, words, and characters in a file.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()  # Read all lines
            num_lines = len(lines)  # Number of lines
            num_words = sum(len(line.split()) for line in lines)  # Number of words
            num_chars = sum(
                len(line) for line in lines
            )  # Number of characters (including spaces)
        return num_lines, num_words, num_chars
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while processing '{file_name}': {e}")
        return None


def main():
    # Check if at least one file is provided
    if len(sys.argv) < 2:
        print("Usage: python file_stats.py <file1> <file2> ... <fileN>")
        sys.exit(1)

    # Iterate over all the files provided on the command line
    for file_name in sys.argv[1:]:
        stats = count_file_statistics(file_name)
        if stats:
            num_lines, num_words, num_chars = stats
            print(f"File: {file_name}")
            print(f"  Lines: {num_lines}")
            print(f"  Words: {num_words}")
            print(f"  Characters: {num_chars}")
            print()


if __name__ == "__main__":
    main()
