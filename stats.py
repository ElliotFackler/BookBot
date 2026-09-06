from collections import Counter

def get_word_count(book_contents):
    words = book_contents.split()
    return len(words)

def get_char_count(book_contents):
    book_contents = book_contents.lower()
    char_counts = {}
    for char in book_contents:
        if (char in char_counts):
            char_counts[char] = char_counts.get(char) + 1
        else:
            char_counts[char] = 1
    #char_counts = dict(Counter(book_contents))
    return char_counts

def chars_dict_to_sorted_list(char_count_dict):
    char_count_list = list(char_count_dict.items())
    sorted_list = sorted(char_count_list, reverse=True, key=sort_on)
    return sorted_list

def sort_on(char_tuple):
    return char_tuple[1]