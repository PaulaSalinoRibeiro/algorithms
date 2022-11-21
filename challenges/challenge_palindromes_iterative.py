def is_palindrome_iterative(word):
    if word == "":
        return False
    result = True
    for index, letter in enumerate(word[: len(word) // 2]):
        reverse_index = -index - 1
        if letter != word[reverse_index]:
            result = False
    return result
