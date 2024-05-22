def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print(f"{word_count} words found in the document.")
    print(letter_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_dicts = []
    letter_count = {}
    text_lowered = text.lower()
    text_filtered = "".join([char for char in text_lowered if char.isalpha()])
    for letter in text_filtered:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    for char, count in letter_count.items():
        letter_dict = {char, count}
        letter_dicts.append(letter_dict)
    return letter_dicts

main()