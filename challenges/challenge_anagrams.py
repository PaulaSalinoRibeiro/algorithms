def is_anagram(first_string, second_string):
    first_word = list(first_string.lower())
    second_word = list(second_string.lower())

    string_first = "".join(merge_sort(first_word))
    string_second = "".join(merge_sort(second_word))

    if first_string == "" and second_string == "":
        anagram = False
    else:
        anagram = string_first == string_second
    return (string_first, string_second, anagram)


def merge(left, right, string):

    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            string[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            string[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        string[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        string[left_cursor + right_cursor] = right[right_cursor]

    return string


def merge_sort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left, right = merge_sort(string[:mid]), merge_sort(string[mid:])
    return merge(left, right, string.copy())
