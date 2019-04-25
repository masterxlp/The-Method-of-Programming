def GenerateSuffixArray(string, length):

    # Generate Suffix Array, store it to list
    suf_array = list()

    start = len(string) - length
    end = len(string)

    while start >= 0:

        suffix = string[start:end]
        suf_array.append(suffix)

        start -= 1
        end -= 1

    return suf_array


def checkRepeat(suf_array):

    # Initialize repeat list
    repeat_list = list()

    # Check Repeat in suffix array
    i = 0
    while i < len(suf_array):

        substr = suf_array[i]

        j = i + 1
        while j < len(suf_array):

            checkStr = suf_array[j]

            if substr == checkStr:
                repeat_list.append(substr)

            j += 1
        i += 1

    if len(repeat_list) == 0:
        return False
    else:
        return repeat_list


def longestRepeatSubstr(string):

    # Compute the length of suffix substring
    max_len = len(string) - 1

    # Initialize the longest repeat substring length to len(string) - 1
    length = max_len

    while length >= 1:

        # Get suffix array
        suf_array = GenerateSuffixArray(string, length)

        # Check repeat
        check_result = checkRepeat(suf_array)

        if check_result is False:
            if length != 1:
                length -= 1
            else:
                print("Don't have repeating substring!")
                break
        else:
            print('The longest repeating substring length is ', length)
            for suf_str in list(check_result):
                print('The longest repeating substring is ', suf_str)
            break


if __name__ == "__main__":
    longestRepeatSubstr('abcd')