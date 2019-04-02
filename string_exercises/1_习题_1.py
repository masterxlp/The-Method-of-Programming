def ReverseString(string):

    # In Python, the str is immutable data type
    # So, transfer the str to list type
    str_list = list(string)

    # Define two pointer i and j to represents the position in string
    i, j = 0, len(string)-1

    # Reverse string
    while i < j:

        # Swap i and j in str_list
        temp = str_list[i]
        str_list[i] = str_list[j]
        str_list[j] = temp

        i += 1
        j -= 1

    return ''.join(str_list)


def ReverseStringPlus(str_list, start, end):

    # This function can realize the local reverse in string

    while start < end:

        temp = str_list[start]
        str_list[start] = str_list[end]
        str_list[end] = temp

        start += 1
        end -= 1


def main(string, m):

    # m means the reverse position in string
    # Transfer string to list
    str_list = list(string)

    # Local reverse
    m %= len(string)
    ReverseStringPlus(str_list, 0, m-1)
    ReverseStringPlus(str_list, m, len(string)-1)
    ReverseStringPlus(str_list, 0, len(string)-1)

    return ''.join(str_list)



if __name__ == "__main__":

    print(ReverseString('July'))
    print(main('July', 2))