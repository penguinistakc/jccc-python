#!/usr/bin/env python3

"""
Rewrite Exercise 2 but this time count the frequency of
each word in the user's input.
A dictionary provides the perfect data structure for this problem.
• Let the words be the keys, and let the counts be the values.
Print the results sorted by the words.
Then, print the results sorted by the counts.
"""

# Initialize an empty set to store unique words
unique_words = set()

# Initialize a dictionary to store word counts
word_count = {}

# Loop to get user input
while True:
    data = input("Enter a line (q to quit): ")
    if data.lower() == 'q':
        break

    # Split the input line into words
    line_words = data.split()

    # Process each word
    for word in line_words:
        word = word.lower()  # Convert to lowercase for case-insensitive processing
        unique_words.add(word)

        # Update the word count in the dictionary
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# Print the unique words (for demonstration)
print("\nUnique words:", unique_words)

# Sort the dictionary keys (words) alphabetically
sorted_words = list(word_count.keys())
sorted_words.sort()

# Print the results sorted by words (alphabetically)
print("\nWord counts sorted by words:")
for word in sorted_words:
    print(f"{word}: {word_count[word]}")

# Sort the dictionary items by counts (in descending order)
sorted_by_count = list(word_count.items())
sorted_by_count.sort(key=lambda item: item[1], reverse=True)

# Print the results sorted by frequency
print("\nWord counts sorted by frequency:")
for word, count in sorted_by_count:
    print(f"{word}: {count}")