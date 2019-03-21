def IsPalindrome(string):

    str_len = len(string)
    # The string is illegal
    if str_len == 0:
        return False
    else:
        # 初始化两个指针
        start = 0
        end = str_len - 1
        # 从两边向中间扫
        while start <= end:
            # 若对应位置字符不同，则返回False
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1

    return True


if __name__ == "__main__":
    print(IsPalindrome('上海自来水来自海上'))