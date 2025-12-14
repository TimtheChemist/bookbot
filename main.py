import sys
from stats import get_num_words
from stats import char_counter

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    return get_book_text(sys.argv[1])

def sort_on(dict_of_characters):
    return dict_of_characters[character]



if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
else:
    number_of_words = get_num_words(main())
    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------""")


    print("Found " + str(number_of_words) + " total words")

    print("""--------- Character Count -------""")

    dict_of_characters = char_counter(main())

    sorted_dict = {k: v for k, v in sorted(dict_of_characters.items(), key=lambda item: item[1], reverse = True)}

    for character in sorted_dict:
        print(character + ": " + str(sorted_dict[character]))


    print("""============= END ===============""")