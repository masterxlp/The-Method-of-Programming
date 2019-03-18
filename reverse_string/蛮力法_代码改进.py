def LeftStringOne(string_list, n):

    # Save the first character
    cache = string_list[0]
    # Swaps characters at two adjacent positions
    for j in range(1, n):
        string_list[j-1] = string_list[j]
    # Move the first character to the last position
    string_list[n-1] = cache

    return string_list


def LeftRotateString(string, m):

    n = len(string)
    # Transfer string to list
    string_list = list(string)
    # Left move character m items
    for i in range(m):
        string_list = LeftStringOne(string_list, n)

    return ''.join(string_list)


if __name__ == "__main__":
    print(LeftRotateString('abcdef', 3))