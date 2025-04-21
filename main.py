from stats import *


def get_book_text(file_path): 
    with open(file_path) as f:
        contents = f.read()
    return contents


def main():
    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words",
--------- Character Count -------"""
)
    sorted_dict_list = sorted_char_dict(char_count_dict(get_book_text("books/frankenstein.txt")))
    for d in sorted_dict_list:
        print(f"{d["character"]}: {d["count"]}")

main()



 