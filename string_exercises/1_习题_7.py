def _set(string):

    lst = list()

    # Store each char in the lst
    i = 0
    while i < len(string):

        if string[i] not in lst:
            lst.append(string[i])

        i += 1

    return lst



def findDoubleFirstChars(string):

    # Transfer string to list
    str_list = list(string)

    # Get each char
    set_lst = _set(string)

    # Count the number of occurrences of each char
    for i in range(len(set_lst)):
        char = set_lst[i]

        j, count = 0, 0

        while j < len(str_list):

            if str_list[j] == char:
                count += 1
            j += 1

        # IF the char occurrences only once, THEN print it
        if count == 1:
            print(set_lst[i])
            break


if __name__ == "__main__":
    findDoubleFirstChars('abaccdeff')