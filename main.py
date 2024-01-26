def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    words_count = get_words_count(book_text)
    characters_count = get_characters_count(book_text)
    characters_count_sorted = get_characters_count_sorted(characters_count)

    print(f"--- Begin report of {path} ---")
    print(f"{words_count} words found in the document\n")
    for character in characters_count_sorted:
        if character[0].isalpha():
            print(f"The '{character[0]}' character was found {character[1]} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_words_count(text):
    words = text.split()
    return len(words)


def get_characters_count(text):
    characters = {}
    for character in text.lower():
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters


def get_characters_count_sorted(characters_dict):
    characters_list = list(characters_dict.items())
    characters_list.sort(key=lambda character: character[1], reverse=True)

    return characters_list


main()
