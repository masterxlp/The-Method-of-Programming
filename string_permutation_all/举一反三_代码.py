def CalcAllPermutation(str_list, lst, num, str_len):

    if num == str_len:
        print(''.join(lst))
    else:
        for i in range(str_len):
            lst.append(str_list[i])
            CalcAllPermutation(str_list, lst, num+1, str_len)
            lst.pop()


def main(string):

    # Transfer string to list
    string_list = list(string)
    lst = list()
    num = 0
    string_len = len(string_list)
    CalcAllPermutation(string_list, lst, num, string_len)


def CalcAllCombination(str_list, lst, num):

    if len(lst) != 0:
        print(''.join(lst))

    for i in range(num, len(str_list)):
        lst.append(str_list[i])
        CalcAllCombination(str_list, lst, i+1)
        lst.pop()


def main2(string):

    # Transfer string to list
    string_list = list(string)
    lst = list()
    num = 0
    CalcAllCombination(string_list, lst, num)

if __name__ == "__main__":
    main2('abc')