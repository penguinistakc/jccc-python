#!/usr/bin/env python3

"""
Use a set to determine the number of unique words in the
user's input.
Use the following to loop through the user's input lines.
while True:
data = input("enter a line (q to quit) ")
if data == 'q':
break
#
# process your lines here
# linewords = data.split()
Output the unique elements sorted alphabetically!
Also, output the number of unique words.
"""

# Initialize an empty set to store unique words
unique_words = set()

# Loop to get user input
while True:
    data = input("Enter a line (q to quit): ")
    if data.lower() == 'q':
        break

    # Split the input line into words
    line_words = data.split()

    # Add each word to the set (automatically handles duplicates)
    for word in line_words:
        unique_words.add(word.lower())  # Convert words to lowercase for case-insensitive uniqueness

# Sort the unique words alphabetically
sorted_unique_words = sorted(unique_words)

# Print the sorted unique words
print("\nUnique words sorted alphabetically:")
for word in sorted_unique_words:
    print(word)

# Print the number of unique words
print(f"\nNumber of unique words: {len(unique_words)}")