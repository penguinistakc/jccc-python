import sys

"""Add exception handling to Exercise 2 so that if a file open
fails, an OSError is handled and the program is halted."""


def main(input_filename, output_filename):
    try:
        # Open the input file for reading and the output file for writing
        infile = open(input_filename, "r")
        outfile = open(output_filename, "w")
        # Copy each line from the input file to the output file
        while True:
            line = infile.readline()
            if not line:  # If end of file is reached, stop
                break
            outfile.write(line)

        infile.close()
        outfile.close()

        print(
            f"File '{input_filename}' has been successfully copied to '{output_filename}'."
        )

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
        sys.exit(1)
    except OSError:
        print(
            f"Error: Unable to read from '{input_filename}' or write to '{output_filename}'."
        )
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Check if the correct number of arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python copy_program.py <input_file> <output_file>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
