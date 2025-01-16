
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(f"Report of {book_path}")
    print(f"{word_count(text)} words in the document")

    work = char_count(text)
    for letter in work:
        print(f"The '{letter}' was found {work[letter]} times")

    print("end report")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(string):
    words = string.split()
    return len(words)

def char_count(text):
    char_count = {}
    text = text.lower()
    #print(text)
    for token in text:
        if token.isalpha():
            if token in char_count:
                char_count[token] += 1
            else:
                char_count[token] = 1
    return char_count
           


main()