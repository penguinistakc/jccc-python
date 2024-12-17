import sys


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
        return 0, 0, 0  # Return zeros for missing files
    except Exception as e:
        print(f"An error occurred while processing '{file_name}': {e}")
        return 0, 0, 0


def main():
    # Check if sufficient arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python file_stats.py [-t] <file1> <file2> ... <fileN>")
        sys.exit(1)

    # Check if the -t option is present
    total_option = False
    file_list = []

    if sys.argv[1] == "-t":
        total_option = True
        file_list = sys.argv[2:]  # Files start from the third argument
    else:
        file_list = sys.argv[1:]  # Files start from the second argument

    if not file_list:
        print("Error: No files specified.")
        sys.exit(1)

    # Initialize total counts
    total_lines, total_words, total_chars = 0, 0, 0

    # Process each file
    for file_name in file_list:
        num_lines, num_words, num_chars = count_file_statistics(file_name)
        if (
            num_lines or num_words or num_chars
        ):  # Only print if file exists and is readable
            print(f"File: {file_name}")
            print(f"  Lines: {num_lines}")
            print(f"  Words: {num_words}")
            print(f"  Characters: {num_chars}")
            print()

        # Update totals
        total_lines += num_lines
        total_words += num_words
        total_chars += num_chars

    # Print total counts if the -t option is specified
    if total_option:
        print("Total Counts Across All Files:")
        print(f"  Lines: {total_lines}")
        print(f"  Words: {total_words}")
        print(f"  Characters: {total_chars}")


if __name__ == "__main__":
    main()
