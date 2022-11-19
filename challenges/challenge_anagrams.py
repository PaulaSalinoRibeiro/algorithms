def is_anagram(first_string, second_string):
    first_word = list(first_string.lower())
    second_word = list(second_string.lower())
    if len(first_word) != len(second_word):
        return False
    for letter in first_word:
        if letter in second_word:
            second_word.remove(letter)
        else:
            return False
    return True
