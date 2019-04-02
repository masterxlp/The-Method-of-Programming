def CountChars(string):

    count = dict()

    for char in string:

        if char in count.keys():
            count[char] += 1
        else:
            count[char] = 1

    return count


if __name__ == "__main__":
    print(CountChars('ABcdEFgH2136511hAc'))