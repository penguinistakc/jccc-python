import sys

"""Create two data files, each with a set of names, one per
line.
Now, write a program that reads both files and lists only those
names that are in both files.
The two file names should be supplied on the command line.
"""


def main():
    # Check if the correct number of command-line arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python common_names.py <file1> <file2>")
        sys.exit(1)

    # Get the file names from the command-line arguments
    file1_name = sys.argv[1]
    file2_name = sys.argv[2]

    try:
        # Read the names from the first file
        with open(file1_name, "r") as file1:
            names1 = set(file1.read().splitlines())  # Store unique names in a set

        # Read the names from the second file
        with open(file2_name, "r") as file2:
            names2 = set(file2.read().splitlines())  # Store unique names in a set

        # Find the common names between the two sets
        common_names = names1.intersection(names2)

        # Print the common names
        if common_names:
            print("Names in both files:")
            for name in sorted(common_names):
                print(name)
        else:
            print("No common names found.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
