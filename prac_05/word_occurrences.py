"""
Word Occurrences
Estimate: 20 minutes
Actual:   15 minutes
"""


def word_occurrences():
    # Prompt user for input
    input_text = input("Text: ")
    # Split the input text into words
    words = input_text.split()
    # Create a dictionary to count occurrences
    word_count = {}
    # Count occurrences of each word
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    # Determine the maximum width for formatting
    max_length = max(len(word) for word in word_count.keys())
    # Sort the dictionary by word
    sorted_words = sorted(word_count.items())
    # Print the results with aligned output
    for word, count in sorted_words:
        print(f"{word:{max_length}} : {count}")

word_occurrences()