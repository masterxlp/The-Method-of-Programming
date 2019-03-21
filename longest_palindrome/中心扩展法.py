def LongestPalindrome(string):

    str_len = len(string)

    # Case 1 The string is illegal
    if str_len == 0:
        return 0

    # Case 2 The string normal
    max_pal_len = 0

    # From the center to both sides
    for center in range(str_len):

        # Case 2.1 The palindrome length is odd
        extend_len = 0
        suc_ex_len = {'cache': 0}
        while center - extend_len >= 0 and center + extend_len < str_len:

            if string[center-extend_len] != string[center+extend_len]:
                break
            # Save the value that has been extended success
            suc_ex_len['cache'] = extend_len
            extend_len += 1

        pal_len = 2 * suc_ex_len['cache'] + 1

        if pal_len > max_pal_len:
            max_pal_len = pal_len

        # Case 2.2 The palindrome length is even
        extend_len = 0
        suc_ex_len = {'cache': 0}

        while center - extend_len >= 0 and center + extend_len + 1 < str_len:

            if string[center-extend_len] != string[center+extend_len+1]:
                break

            suc_ex_len['cache'] = extend_len
            extend_len += 1

        pal_len = 2 * suc_ex_len['cache'] + 2

        if pal_len > max_pal_len:
            max_pal_len = pal_len

    return max_pal_len


if __name__ == "__main__":
    print(LongestPalindrome('abcbaccctvvtcc'))