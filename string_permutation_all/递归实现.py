def swap(lst, pa, pb):

    # Swap the character of pa and pb position
    char = lst[pa]
    lst[pa] = lst[pb]
    lst[pb] = char

    return lst



def CalcAllPermutation(string_list, start, end):

    # end <= 1 means the string is None
    if end <= 1:
        return
    elif start == end:
        print(''.join(string_list))
    else:
        for j in range(start, end):
            print(j, start, string_list)
            swap(string_list, start, j)
            print(j, start, string_list)
            CalcAllPermutation(string_list, start+1, end)
            # 复原原字符串序列
            print(j, start, string_list)
            swap(string_list, start, j)
            print(j, start, string_list)


if __name__ == "__main__":
    string = 'abc'
    string_lst = list(string)
    CalcAllPermutation(string_lst, 0, len(string_lst))