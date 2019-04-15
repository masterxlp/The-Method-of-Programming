def deleteSpecialChars(raw_str, pattern_str):

    # Transfer raw_str to list
    raw_str_list = list(raw_str)

    # Delete special chars of pattern string in raw string
    for i in range(len(pattern_str)):

        pattern_char = pattern_str[i]

        j = 0
        while j < len(raw_str):

            if raw_str_list[j] == pattern_char:
                raw_str_list[j] = ' '

            j += 1

    return ''.join(raw_str_list)


def deleteSpecialChars2(raw_str, pattern_str):

    # Transfer raw_str to list
    raw_str_list = list(raw_str)

    # Use list store the pattern element position in raw string
    index_list = list()

    for i in range(len(raw_str_list)):

        if raw_str_list[i] in pattern_str:
            index_list.append(i)

    # Sort index list in ascending order, in order to delete the pattern
    # element , and Guarantee the index doesn't exceed the list length
    index_list = sorted(index_list, reverse= True)

    for j in index_list:
        raw_str_list.pop(j)

    return ''.join(raw_str_list)


if __name__ == "__main__":
    print(deleteSpecialChars('They are students.', 'aeiou'))
    print(deleteSpecialChars2('They are students.', 'aeiou'))