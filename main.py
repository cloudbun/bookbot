def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_dict = letter_count(text)
    pretty_print(book_path, num_words, letter_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()

def letter_count(text):
    chars = {}
    for character in text:
        lowered = character.lower()
        if lowered in chars and lowered.isalpha():
            chars[lowered] += 1
        elif lowered.isalpha():
            chars[lowered] = 1
    return chars
    
def pretty_print(book_path, num_words, letter_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for item in sorted(letter_dict.items(), reverse = True, key = lambda item: item[1]):
        print(f"The '{item[0]}' character was found {item[1]} times.")
    print("--- End report ---")

if __name__ == "__main__":
    main()