#!/usr/bin/env python3

import subprocess

# Initial list
data = ["mike", "jane", "alice", "ruth"]

# Join the list into a single string with newlines, as sort expects line-separated input
input_data = "\n".join(data)

# Run the 'sort' command using subprocess.run
result = subprocess.run(
    ["sort"],  # The shell command to execute
    input=input_data,  # Pass the list data as input to the command
    text=True,  # Enable text mode (string I/O)
    capture_output=True,  # Capture the command's standard output
)

# Store the sorted output into a new list
sorted_data = result.stdout.splitlines()

# Print the sorted list element by element
print("Sorted List:")
for element in sorted_data:
    print(element)
