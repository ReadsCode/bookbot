from stats import word_count, char_count_dict


def get_book_text(file_path): 
    with open(file_path) as f:
        contents = f.read()
    return contents

        

word_count = word_count(get_book_text("books/frankenstein.txt"))

print(f"{word_count} words found in the document")

print(char_count_dict(get_book_text("books/frankenstein.txt")))



