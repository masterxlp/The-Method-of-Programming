"""
******************************************************************
@Title: 均分 01
@Method: 1. 由于最后可进行子串的拼接，所以字符串可看为一个圆环；
         2. 又因为位于圆环上的0和1的个数为均为偶数；
         3. 且均分后的两部分0和1在每一部分的个数均为总数的一半；
         4. 于是，问题变为：如何在字符串圆环上找到一条可以均分01的直径；
         5. 解4的思路为：从当前位置i开始，顺时针方向寻找1/2 len(string)长度的子串
            位置为j，若该子串满足0和1的个数均为字符串中0和1总个数的一半，则寻找成功，
            否则i+1，直到找到满足该条件的位置i，j（即满足条件的直径的位置）；
         6. 由此可见，对于满足条件的字符串，只需通过1次或者2次切分实现均分；
******************************************************************
"""


def map01(string):

    # Map and count 01
    # Initialize dictionary
    map_result = {'0': 0, '1': 0}
    for char in string:
        if char is '0':
            map_result['0'] += 1
        else:
            map_result['1'] += 1

    return map_result


def check01TotalNum(sub_str, total0, total1):

    # Check the 0's and 1's number in the substring
    # Map the number use dictionary
    check_result = map01(sub_str)
    if check_result['0'] == total0 and check_result['1'] == total1:
        return True

    return False




def AverageDivide01(string):

    # Initialize diameter
    dia_len = len(string) // 2

    # Count the number of 0 and 1 in string
    count = map01(string)
    total0 = count['0'] // 2
    total1 = count['1'] // 2

    # Illegal input
    if len(string) > 100:
        print('The input string length is illegal!')

    # Illegal input -- even number
    elif count['0'] % 2 != 0 or count['1'] % 2 != 0:
        print("The input string contains an odd number of zeros or ones!")

    else:
        # Find the position of diameter in the circle where the number of 0's
        # and 1's in the substring is half the total number of 0's and 1's in
        # the string
        # Initialize the start position of diameter
        i = 0
        while i < len(string):

            j = i + dia_len
            sub_str = string[i:j]
            check_result = check01TotalNum(sub_str, total0, total1)
            if check_result is True:
                print('The start split position is %d, and the end position is %d' % (i, j-1))
                print('The substring is %s %s %s' % (string[:i], sub_str, string[j:]))
                break
            else:
                i += 1


if __name__ == '__main__':
    AverageDivide01('010111')