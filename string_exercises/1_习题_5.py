def CompressedStringSpace(string):

    # Count the number of occurrences of Spaces
    count = 0

    # Create a new string, use list store the item in new string
    new_string = list()

    # Compressed String Space
    i = 0
    compress = ' '
    while i < len(string):

        if string[i] is not compress:
            if count != 0:
                new_string.append(compress)
            new_string.append(string[i])
            count = 0
        else:
            count += 1

        i += 1

    return new_string


def reverse(str_list, start, end):

    # Reverse string
    while start < end:

        temp = str_list[start]
        str_list[start] = str_list[end]
        str_list[end] = temp

        start += 1
        end -= 1

    return str_list


def main(string):

    str_list = CompressedStringSpace(string)

    # Create reversed string
    rev_str = list()

    # Reverse substring
    j = 0
    sub_str = list()
    while j < len(str_list):

        if str_list[j] is ' ':
            if len(sub_str) != 0:
                rev_sub_str = reverse(sub_str, 0, len(sub_str)-1)
                rev_str.append(''.join(rev_sub_str))
                for i in range(len(sub_str)):
                    sub_str.pop()

            rev_str.append(str_list[j])

            j += 1
        else:
            sub_str.append(str_list[j])

            if j == len(str_list) - 1:
                if len(sub_str) > 1:
                    rev_sub_str = reverse(sub_str, 0, len(sub_str) - 1)
                    rev_str.append(''.join(rev_sub_str))
                    for i in range(len(sub_str)):
                        sub_str.pop()
                else:
                    rev_str.append(str_list[j])

            j += 1

    return ''.join(rev_str)


if __name__ == "__main__":
    print(main(' I   am  a   student  , and  you ？'))