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


def isExist(long_suf_str, short_suf_str):

    check_result = list()

    # Check whether the Map is success
    for long_char in long_suf_str:

        if long_char in short_suf_str:
            check_result.append(long_char)

    return check_result


def longestCommonSubstr(strA, strB):

    min_len = min(len(strA), len(strB))

    # Initialize the length to min length in strA and strB length
    length = min_len

    # Rest longest string and shortest string
    if len(strA) >= len(strB):
        long_str = strA[:]
        short_str = strB[:]
    else:
        long_str = strB[:]
        short_str = strA[:]

    while length >= 1:

        # Gets the suffix array
        long_suf_array = GenerateSuffixArray(long_str, length)
        short_suf_array = GenerateSuffixArray(short_str, length)

        # Checks whether elements in the longest suffix array exist in
        # the shortest suffix array
        check_result = isExist(long_suf_array, short_suf_array)

        if len(check_result) == 0:
            length -= 1
        else:
            print(check_result[len(check_result)-1])
            break


if __name__ == '__main__':
    longestCommonSubstr('abcdabc', 'vabcdcfdabc')