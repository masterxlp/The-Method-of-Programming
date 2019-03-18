def LeftRotateString(string, m):

    # Transfer the string to list
    string_list = list(string)

    # Move one character to the list left station
    # Repetition the process m times
    n = len(string_list)
    for i in range(m):
        cache = string_list[0]
        for j in range(1, n):
            string_list[j-1] = string_list[j]
        string_list[n-1] = cache

    # Transfer the list to string and return result
    return ''.join(string_list)


if __name__ == "__main__":
    print(LeftRotateString('abcdef', 3))