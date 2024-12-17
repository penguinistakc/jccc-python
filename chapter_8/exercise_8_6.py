import sys
from collections import defaultdict


def main():
    # Check if at least one file is supplied
    if len(sys.argv) < 2:
        print("Usage: python count_lines.py <file1> <file2> ... <fileN>")
        sys.exit(1)

    # Dictionary to count occurrences of each line
    line_counts = defaultdict(int)

    # Iterate through all the file names supplied as command-line arguments
    for file_name in sys.argv[1:]:
        try:
            # Read lines from the current file
            with open(file_name, "r") as file:
                for line in file:
                    # Strip newline characters and increment count for the line
                    line_counts[line.strip()] += 1
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found. Skipping.")
        except Exception as e:
            print(f"An error occurred while processing '{file_name}': {e}")

    # Print the line counts
    print("\nLine occurrence counts across all files:")
    for line, count in sorted(line_counts.items()):
        print(f"'{line}': {count} times")


if __name__ == "__main__":
    main()
