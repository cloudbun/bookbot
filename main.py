import sys
from stats import count_words, create_char_dict, create_dictionary, print_char_freq

def get_book_text(filepath):
    with open(filepath) as file:
        input = file.read()
    return input

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f'Found {count_words(text)} total words')
    print("--------- Character Count -------")
    print_char_freq(create_dictionary(create_char_dict(text)))
    print("============= END ===============")

if __name__ == "__main__":
    main()
