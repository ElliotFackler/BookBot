from collections import Counter
import string

# Get and return the word count of the txt file
def get_word_count(book_contents) -> int:
    words = book_contents.split()
    return len(words)

# Iterate through the words and find the five most common and return them
def get_most_common_words(book_contents) -> list:
    lowercase = book_contents.lower()
    lowercase_with_no_punctuation = lowercase.translate(str.maketrans("", "", string.punctuation))
    words = lowercase_with_no_punctuation.split()
    word_counts = {}
    for word in words:
        if (word in word_counts):
            word_counts[word] = word_counts.get(word) + 1
        else:
            word_counts[word] = 1

    i = 0
    five_most_common_words = {}
    while i < 5:
        most_common_word = max(word_counts, key=word_counts.get)
        five_most_common_words[i] = (most_common_word, max(word_counts.values()))
        del word_counts[most_common_word]
        i = i + 1

    return five_most_common_words

# Get the character count of the txt file
def get_char_count(book_contents) -> dict:
    book_contents = book_contents.lower()
    char_counts = {}
    for char in book_contents:
        if (char in char_counts):
            char_counts[char] = char_counts.get(char) + 1
        else:
            char_counts[char] = 1
    return char_counts

# Convert the character dictionary into a list sorted by number of appearances of each character
def chars_dict_to_sorted_list(char_count_dict) -> list:
    char_count_list = list(char_count_dict.items())
    sorted_list = sorted(char_count_list, reverse=True, key=sort_on)
    return sorted_list

# Return the second element of a tuple so the list is sorted by the value
def sort_on(char_tuple) -> int:
    return char_tuple[1]