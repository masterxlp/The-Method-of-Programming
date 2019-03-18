def _int_iter():

    # 生成器生成从3开始的无限序列
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):

    # 筛选函数
    return lambda x: x % n > 0


def primes():

    # 先返回一个2
    yield 2
    # 初始序列
    it = _int_iter()
    while True:
        # 返回序列的第一个数
        n = next(it)
        yield n
        # 构造新序列
        it = filter(_not_divisible(n), it)


def GeneratePrimeNumber(m):

    pri_num_list = list()

    i = 0
    for n in primes():
        if i < m:
            pri_num_list.append(n)
            i += 1
        else:
            break

    return pri_num_list


def MapStringToPrimes(string, prime_list, corps):

    prime = list()
    for char in string:
        position = corps.index(char)
        prime.append(prime_list[position])

    total = 1
    for num in prime:
        total *= num

    return total, prime


def GeneratePrimeList(string, corps_dict):

    # Gets the all characters
    corps = list(string)
    for key in corps_dict.keys():
        corps += list(key)
    corps = set(corps)
    corps = list(corps)

    # Generate prime list of all string
    length = len(corps)
    prime_list = GeneratePrimeNumber(length)

    return prime_list, corps


def FindBrotherString(string, corps_dict):

    # Get prime list
    prime_list, corps = GeneratePrimeList(string, corps_dict)

    # Compute the total prime of string
    origin_string_value, _ = MapStringToPrimes(string, prime_list, corps)
    brother_string_list = list()
    for key in corps_dict.keys():
        num, _ = MapStringToPrimes(key, prime_list, corps)
        if num == origin_string_value:
            brother_string_list.append(key)

    return brother_string_list


def GenerateSign(string, prime_list, corps):

    # Gets the minimal prime number in prime_list
    minimal_prime = min(prime_list)

    _, prime = MapStringToPrimes(string, prime_list, corps)

    # Compute sign of string
    sign = 0
    for num in prime:
        sign |= (1 << (num - minimal_prime))

    return sign


def GenerateIndexList(string, corps_dict):

    # Initial list use string
    corps_list = list(string)
    # Gets the all unique char
    for key in corps_dict.keys():
        corps_list += list(key)

    corps_list = list(set(corps_list))

    # Generate the unique index
    index_list = list()
    for i in range(1, len(corps_list)+1):
        index_list.append(i)

    return index_list, corps_list


def FindStringContain(string, corps_dict):

    # Gets the prime list
    prime_list, corps = GeneratePrimeList(string, corps_dict)

    # Find brother string via sign
    sign = GenerateSign(string, prime_list, corps)

    brother_string_list = list()
    for chars in corps_dict.keys():
        _sign = GenerateSign(chars, prime_list, corps)
        if sign ^ _sign == 0:
            brother_string_list.append(chars)

    return brother_string_list


def FindStringContain2(string, corps_dict):
    # Gets the prime list
    index_list, corps_list = GenerateIndexList(string, corps_dict)

    # Find brother string via sign
    sign = GenerateSign(string, index_list, corps_list)

    brother_string_list = list()
    for chars in corps_dict.keys():
        _sign = GenerateSign(chars, index_list, corps_list)
        if sign ^ _sign == 0:
            brother_string_list.append(chars)

    return brother_string_list



if __name__ == "__main__":
    print(FindBrotherString('bad', {'bad': None, 'abd': None, 'dba': None,
                                    'cba': None, 'cab': None, 'efb': None,
                                    'dcj': None, 'klh': None, 'dab': None,
                                    'bda': None, 'adb': None, 'dbb': None}))
    print(FindStringContain('bad', {'bad': None, 'abd': None, 'dba': None,
                                     'cba': None, 'cab': None, 'efb': None,
                                     'dcj': None, 'klh': None, 'dab': None,
                                     'bda': None, 'adb': None, 'dbb': None}))
    print(FindStringContain2('bad', {'bad': None, 'abd': None, 'dba': None,
                                     'cba': None, 'cab': None, 'efb': None,
                                     'dcj': None, 'klh': None, 'dab': None,
                                     'bda': None, 'adb': None, 'dbb': None}))