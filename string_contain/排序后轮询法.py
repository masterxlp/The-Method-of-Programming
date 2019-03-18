def StringContain(long_str, short_str):

    # In order to sort it, transfer string to list
    long_str_list = list(long_str)
    short_str_list = list(short_str)

    # Sort list
    long_str_list.sort()
    short_str_list.sort()
    # print(long_str_list, short_str_list)

    # Polling character from short string to long string
    long_len = len(long_str_list)
    short_len = len(short_str_list)
    for ps in range(short_len):
        short_chars = short_str_list[ps]
        pl = 0
        while pl < long_len and long_str_list[pl] < short_chars:
            pl += 1
        if pl >= long_len or short_chars > long_str_list[pl]:
            return False
    return True


if __name__ == "__main__":
    print(StringContain('ACBD', 'ACB'))