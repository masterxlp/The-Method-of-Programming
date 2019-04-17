def longestContinuousChars(string, info):

    if len(string) == 0:
        value = max([value for value in info.values()])
        print("The longest continuous char's length is ", value)
        lst = [chars * value for chars in info.keys() if info[chars] == value]
        chars = ' and '.join(lst)
        print("The longest continuous chars is ", chars)
    else:
        char = string[0]

        if char in info.keys():
            info[char] += 1
        else:
            info[char] = 1

        string = string[1:]
        longestContinuousChars(string, info)


if __name__ == "__main__":
    longestContinuousChars('aaabbb', {})