
def main():
    path = "books/frankenstein.txt"
    book_contents = get_book_text(path)
    word_count = get_word_count(book_contents)
    print(f"Found {word_count} total words")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(book_contents):
    words = book_contents.split()
    return len(words)


if __name__ == "__main__":
    main()