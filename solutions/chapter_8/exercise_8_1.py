"""Write a program that asks the user for the names of an
input and an output file.
Open both of these files and then have the program read from
the input file (use readline) and write to the output file (use
write).
• In effect, this is a copy program.
• The interface to the program might look like:
Enter the name of the input file: myinput
Enter the name of the output file: myoutput
"""


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
    # Ask the user for the names of the input and output files
    input_filename = input("Enter the name of the input file: ")
    output_filename = input("Enter the name of the output file: ")

    main(input_filename, output_filename)
