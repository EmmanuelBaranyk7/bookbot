def get_num_words(text):
    return len(text.split())

def char_count_dict(text):
    count = {}
    text = text.lower()

    for symbol in text:
            if symbol in count:
                count[symbol] += 1
            else:
                count[symbol] = 1

    return count


def sort_dict(dict):
    return dict["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_dict)
    return sorted_list