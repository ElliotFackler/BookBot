from stats import get_word_count, get_char_count, chars_dict_to_sorted_list
import sys

def main():
    is_input_valid(sys.argv)
    path = sys.argv[1]
    book_contents = get_book_text(path)
    word_count = get_word_count(book_contents)
    char_count = get_char_count(book_contents)
    sorted_list = chars_dict_to_sorted_list(char_count)
    print_report(path, word_count, sorted_list)

# Pull the text from the file
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# Produce a refined report of the book's stats
def print_report(path1, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path1}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for i in sorted_list:
        if i[0].isalpha() == True:
            print(f"{i[0]}: {i[1]}")

def is_input_valid(input):
    if (len(input) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

if __name__ == "__main__":
    main()