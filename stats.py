def get_number_of_words(text):
    return len(text.split())


def get_characters_count(text):
    char_count_dict = {}

    for c in text.lower():
        if c in char_count_dict:
            char_count_dict[c] += 1
        else:
            char_count_dict[c] = 1
    
    return char_count_dict


def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), reverse=True, key=lambda item: item[1]))