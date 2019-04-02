def swap(lst, i, j):

    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def LeftShiftLetters(str_list):

    # Pointer i and j means the chars * and letter
    # Initialize two pointer
    i, j = 0, 0

    # Left Shift letters
    while j < len(str_list):

        # Find the first position of *
        if str_list[i] != '*':

            i += 1

        # Guarantee only move the letter locate on * right
        if j < i:
            j = i

        # Find the letter position
        if str_list[j] == '*':

            if j < len(str_list)-1:
                j += 1
                continue
            else:
                break

        swap(str_list, i, j)

        # Guarantee pointer i is the first * position
        i += 1

    return str_list, i


def Reverse(str_list, start, end):

    # Move the letter to right
    while start < end:
        temp = str_list[start]
        str_list[start] = str_list[end]
        str_list[end] = temp
        start += 1
        end -= 1


def main(string):

    str_list = list(string)
    str_list, i = LeftShiftLetters(str_list)
    Reverse(str_list, 0, i-1)
    Reverse(str_list, 0, len(str_list)-1)

    return ''.join(str_list)


if __name__ == "__main__":
    print(main('G*A*B*C*D*F*E*C'))