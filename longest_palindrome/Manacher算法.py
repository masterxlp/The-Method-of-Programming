def AddSpecialChars(string):

    new = '$'
    for i in range(len(string)):
        new += '#' + string[i]

    return new + '#'


def Manacher(string):

    str_len = len(string)

    # Initialize the maximum palindrome substring boundary
    mx = 0
    # Initialize the array list p and ID
    p = [0] * str_len
    # ID means the extended num when the center is i
    ID = 0
    # Manacher Programming
    for i in range(1, str_len):

        # Initialize the p[i] and Compute p[i]

        # Initialize p[i]
        # Case 1. If the mx > i, then p[i] >= min(p[2 * id - i], mx - i)
        if mx > i:
            p[i] = min(p[2 * ID - i], mx - i)
        else:
            # Case 2. If the mx <= i, then p[i] = 1
            p[i] = 1

        # Compute p[i]
        # Compare the characters on the both sides of the center i
        # IF the same, p[i] += 1; ELSE break
        while i+p[i] < str_len and string[i+p[i]] == string[i-p[i]]:
            p[i] += 1

        # Compute mx and ID
        if p[i] + i > mx:
            mx = p[i] + i
            ID = i
    return p


def LongestPalindrome(lst, new_string):

    # return max(lst) - 1
    pal_center = lst.index(max(lst))
    length = max(lst) - 1
    pal = new_string[pal_center-length:pal_center+length+1]

    return pal.replace('#', '')


if __name__ == "__main__":
    char = AddSpecialChars('12212321')
    lyst = Manacher(char)
    print(LongestPalindrome(lyst, char))