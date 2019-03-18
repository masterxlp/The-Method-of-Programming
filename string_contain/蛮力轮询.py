def StringContain(longStr, shortStr):

    longLength = len(longStr)
    shortLength = len(shortStr)

    for i in range(shortLength):
        shortChars = shortStr[i]
        for j in range(longLength):
            longChars = longStr[j]
            if shortChars is longChars:
                break
            elif j == longLength - 1:
                return False
    return True

if __name__ == "__main__":
    print(StringContain('ABCD', 'AE'))