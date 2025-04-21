from stats import *
import sys

def get_book_text(file_path): 
    with open(file_path) as f:
        contents = f.read()
    return contents


def main(book):
    print(f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {word_count(get_book_text(book))} total words",
--------- Character Count -------"""
)
    sorted_dict_list = sorted_char_dict(char_count_dict(get_book_text(book)))
    for d in sorted_dict_list:
        print(f"{d["character"]}: {d["count"]}")
    
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



book_path = sys.argv[1]
main(book_path)



 