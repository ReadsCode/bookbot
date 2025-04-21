def word_count(book_s):
    w_count = 0
    words = book_s.split()
    for w in words:
        w_count += 1
    return w_count

def char_count_dict(book_s):
    char_dict = {}
    for c in book_s:
        lower_case_c = c.lower()
        if lower_case_c in char_dict:
            char_dict[lower_case_c] += 1
        else:
            char_dict.update({lower_case_c : 1})
    return char_dict

def sorted_char_dict(char_dict):
    sorted_dicts = []
    for key in char_dict:
        if key.isalpha():
            temp_dict = {"character": key, "count": char_dict[key]}
            sorted_dicts.append(temp_dict)
    sorted_dicts.sort(reverse=True, key=lambda x: x["count"])
    return sorted_dicts



