def num_words(text):
    return len(text.split())

def char_count(text):
    count = {}
    text = text.lower()

    for symbol in text:
        if symbol.isalpha():
            if symbol in count:
                count[symbol] += 1
            else:
                count[symbol] = 1

    return count

def 
