def count_words(text_input):
    words = text_input.split()
    return len(words)

def create_char_dict(text_input):
    # Takes text -> returns num of each character
    char_dict = {}
    for character in text_input:
        lower = character.lower()
        if lower in char_dict:
            char_dict[lower] += 1
        else:
            char_dict[lower] = 1
    return char_dict

def create_dictionary(input_dict, descending = True):
    return [
        {"character": key, "occurrence": value}
        for key, value in sorted(
            input_dict.items(),
            key=lambda x: x[1], # Works bc it's grabbing the next field
            reverse=descending
        )
    ]

def print_char_freq(input_dict):
    alpha_chars = (
        f"{item['character']}: {item['occurrence']}"
        for item in input_dict if item['character'].isalpha()
    )
    print(*alpha_chars, sep="\n")
