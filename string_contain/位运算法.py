def getASCIIValue(string):

    ascii_list = list()
    for i in range(len(string)):
        chars = string[i]
        ascii_value = ord(chars)
        ascii_list.append(ascii_value)

    return ascii_list


def StringContain(long_str, short_str):

    # Gets the ASCII value of the characters in the string
    long_str_ascii = getASCIIValue(long_str)
    short_str_ascii = getASCIIValue(short_str)

    # Gets the signature of the characters in the string
    sign = 0
    for i in range(len(long_str_ascii)):
        # 这里减'A'的原因在于避免数值太大
        # 通过按位或的运算为字符串中的所有唯一字符进行签名（体现在二进制位为1上）
        sign |= (1 << (long_str_ascii[i] - ord('A')))
    # print(sign)

    for j in range(len(short_str_ascii)):
        # 通过字符串中的每一个字符进行按位与运算的结果来判断是否包含：若包含则
        # 其按位与运算结果不为0，否则为0
        if (sign & (1 << (short_str_ascii[j]) - ord('A'))) == 0:
            return False

    return True


if __name__ == "__main__":
    print(StringContain('ABCD', 'AB'))