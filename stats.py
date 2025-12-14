import string

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    word_count = len(text.split())
    return word_count

all_characters = string.printable
dict = {}

def char_counter(text):
    for character in all_characters:
        character_counter = 0
        for position in text:
            if character == position.lower():
                character_counter += 1
        dict[character] = character_counter

    for character in all_characters:
        if character.isupper() == True:
            dict.pop(character, None)

    return dict

