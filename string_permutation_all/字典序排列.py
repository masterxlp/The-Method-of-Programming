def swap(lst, pa, pb):

    num = lst[pa]
    lst[pa] = lst[pb]
    lst[pb] = num

    return lst


def reverse(lst, start, end):

    while start <= end:
        swap(lst, start, end)
        start += 1
        end -= 1

    return lst


def CalcAllPermutation(string_list):

    str_len = len(string_list)
    i = str_len - 2
    while True:
        # 1. 寻找排列中最右一个升序的首位位置i
        if i >= 0 and string_list[i] >= string_list[i+1]:
            i -= 1
        elif i < 0:
            return False
        else:
            break
    # pa = i

    j = str_len - 1
    while True:
        # 2. 寻找排列中第i位右边最后一个比string_list[i]大的位置j
        if j > i and string_list[j] <= string_list[i]:
            j -= 1
        else:
            break
    # pb = j

    # 3. 交换string_list[i]与string_list[j]
    swap(string_list, i, j)

    # 4. 翻转i+1至字符串末尾的子串
    reverse(string_list, i+1, str_len-1)

    return string_list


def main(string):

    # Transfer string to list
    string_list = list(string)
    string_list = sorted(string_list)
    # Gets all permutation of string
    perm = list()
    perm.append(''.join(string_list))

    result = CalcAllPermutation(string_list)
    while result is not False:
        perm.append(''.join(result))
        result = CalcAllPermutation(result)

    return perm

if __name__ == '__main__':
    print(main('acb'))