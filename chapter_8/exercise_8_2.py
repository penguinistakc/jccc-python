import sys


def main(input_filename, output_filename):
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


if __name__ == "__main__":
    # Check if the correct number of arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python copy_program.py <input_file> <output_file>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
