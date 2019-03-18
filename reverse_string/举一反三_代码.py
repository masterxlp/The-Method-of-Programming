def ReverseWords(string):

    string_list = string.split()
    end = len(string_list)-1
    start = 0
    while start < end:
        cache = string_list[start]
        string_list[start] = string_list[end]
        string_list[end] = cache
        start += 1
        end -= 1
    return ' '.join(string_list)


def ReverseString(string_list, start, end):

    while start < end:
        cache = string_list[start]
        string_list[start] = string_list[end]
        string_list[end] = cache
        start += 1
        end -= 1


def ReverseRotateString(string):

    # Transfer string to list
    string_list = list(string)
    indicator = ' '
    n = len(string_list)
    start = 0
    for i in range(n):
        chars = string_list[i]
        if chars == indicator:
            ReverseString(string_list, start, i-1)
            start = i + 1
        elif i == n-1:
            ReverseString(string_list, start, i)
            start = i + 1

    ReverseString(string_list, 0, n-1)
    return ''.join(string_list)


if __name__ == "__main__":
    print(ReverseWords('I am a student.'))
    print(ReverseRotateString('I am a student.'))