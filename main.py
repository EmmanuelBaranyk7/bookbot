from stats import num_words
from stats import char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(get_book_text('books/frankenstein.txt'))} total words")
    print("--------- Character Count -------")
    print(char_count(get_book_text('books/frankenstein.txt')))    

main()