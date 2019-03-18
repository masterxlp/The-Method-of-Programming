def ReverseString(string_list, start, end):

    # Swaps characters in relative position
    while start < end:
        cache = string_list[start]
        string_list[start] = string_list[end]
        string_list[end] = cache
        start += 1
        end -= 1


def LeftRotateString(string, m):

    # Transfer the string to list
    string_list = list(string)
    n = len(string_list)
    m %= n
    ReverseString(string_list, 0, m-1)
    ReverseString(string_list, m, n-1)
    ReverseString(string_list, 0, n-1)

    return ''.join(string_list)


if __name__ == "__main__":
    print(LeftRotateString('abcdef', 3))