import datetime


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


def PrintSequence(str_list, lst, lyst, num):

    if len(lst) != 0:
        char = '('
        for j in range(len(lst)):
            if j < len(lst) - 1:
                char += lst[j] + ','
            else:
                char += lst[j] + ')'
        lyst.append(char)

    for i in range(num, len(str_list)):
        lst.append(str_list[i])
        PrintSequence(str_list, lst, lyst, i+1)
        lst.pop()

    return lyst


def main3(string):

    # Transfer string to list
    string_list = list(string)
    lst, lyst = list(), list()
    num = 0
    lyst = PrintSequence(string_list, lst, lyst, num)

    # 按照各元素的长度进行排序
    lyst = sorted(lyst, key=lambda x: len(x))

    # 打印结果
    for i in range(len(lyst)-1):
        if len(lyst[i]) == len(lyst[i+1]):
            print(u'{}'.format(lyst[i]), end=',')
        else:
            print(u'{}'.format(lyst[i]), end='\n')
    print(u'{}'.format(lyst[len(lyst)-1]), end='')


if __name__ == "__main__":
    start = datetime.datetime.now()
    main3('abcdefghigklmnopqrstuvwxyz')
    end = datetime.datetime.now()
    print("Use time is", start - end)