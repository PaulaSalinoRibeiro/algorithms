def compare_word(first_word, second_word):
    for letter in first_word:
        if letter in second_word:
            second_word = second_word.replace(letter, "", 1)
        else:
            return False

    return True


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    if first_string == "" or second_string == "":
        return False

    first_word, second_word = first_string.lower(), second_string.lower()

    return compare_word(first_word, second_word)
