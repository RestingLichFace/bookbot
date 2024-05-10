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
    letter_count = {}
    text_lowered = text.lower()
    for letter in text_lowered:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

main()