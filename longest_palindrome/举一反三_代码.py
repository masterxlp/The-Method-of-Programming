def AddSpecialChar(string):

    # Add the # and $ in string
    char = '$'
    for i in range(len(string)):
        char += '#' + string[i]

    char += '#'

    return char


def Manacher(string):

    # Initialize the array list p that store the extend length to left,
    # Include string[i]
    str_len = len(string)
    p = [0] * str_len

    # Initialize the center of the longest palindrome string
    center = 0

    # Initialize the boundary of the longest palindrome string
    mx = 0

    # Start the manacher programming
    #
    for i in range(1, str_len):

        # Case 1. IF mx > i, THEN p[i] >= min(p[2*center-i], mx-i)
        if mx > i:
            p[i] = min(p[2 * center - i], mx - i)
        else:
            # Case 2. IF mx <= i, THEN set p[i] = 1
            p[i] = 1

        # Expand to both sides with i as the center and update p[i] value
        while p[i] + i < str_len and string[p[i] + i] == string[i - p[i]]:
            p[i] += 1

        # Update mx value and center value
        if p[i] + i > mx:
            mx = p[i] + i
            center = i

    return p


def SplitPalindrome(lst, string):

    _lst = lst[:]
    _string = string[:]
    _lst = sorted(_lst, reverse=True)
    i = 0
    while i < len(_lst):

        # Case 1. The longest palindrome substring length is greater than 2
        n = max(_lst)
        if n > 2:
            pal_center = lst.index(n)
            length = n - 1
            pal = string[pal_center-length:pal_center+length+1]

            # Keep the palindrome substring length constant
            pal = ',' + pal[1:len(pal)] + ','
            pal = pal.replace('#', ' ')

            # Make the palindrome substring p value equal 0
            for j in range(pal_center-length, pal_center+length+1):
                lst[j] = 0

            _lst = lst[:]
            _lst = sorted(_lst, reverse=True)

            # Replace the palindrome substring with an equally long string
            _string = _string[:pal_center-length] + pal + _string[pal_center+length+1:]

        i += 1

    _string = _string.replace('#', ',').replace('$', '').replace(' ', '')

    if _string[0] is ',':
        _string = _string[1:]
    if _string[len(_string)-1] is ',':
        _string = _string[:len(_string)-1]

    return _string


if __name__ == "__main__":
    chars = AddSpecialChar('habbafghabbahg')
    lyst = Manacher(chars)
    print(lyst)
    print(SplitPalindrome(lyst, chars))