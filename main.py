from stats import get_number_of_words, get_characters_count, sort_dict_by_value
import sys

def get_book_text(path):
    with open(path, "r") as book:
        return book.read()

def main():
    try:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        words_in_book = get_number_of_words(book_text)
        characters_in_book = get_characters_count(book_text)
        characters_in_book = sort_dict_by_value(characters_in_book)
        print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_path}
    ----------- Word Count ----------
    Found {words_in_book} total words
    --------- Character Count -------""")
        for character in characters_in_book:
            if character.isalpha():
                print(f"{character}: {characters_in_book[character]}")
    except IndexError as index_error:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
