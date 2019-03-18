from functools import reduce
import operator

def StringContain(long_str, short_str):

    # Map 26 English letters to 26 prime Numbers
    letters_map_dict = {'A': 2, 'B': 3, 'C': 5, 'D': 7, 'E': 11,
                        'F': 13, 'G': 17, 'H': 19, 'I': 23, 'J': 29,
                        'K': 31, 'L': 37, 'M': 41, 'N': 43, 'O': 47,
                        'P': 53, 'Q': 59, 'R': 61, 'S': 67, 'T': 71,
                        'U': 73, 'V': 79, 'W': 83, 'X': 89, 'Y': 97,
                        'Z': 101}

    # Map characters in string to prime number
    long_prime_number_list = list()
    short_prime_number_list = list()
    for char in long_str:
        prime_number = letters_map_dict[char]
        long_prime_number_list.append(prime_number)
    for char in short_str:
        prime_number = letters_map_dict[char]
        short_prime_number_list.append(prime_number)

    long_prime = reduce(operator.mul, long_prime_number_list, 1)
    short_prime = reduce(operator.mul, short_prime_number_list, 1)

    if long_prime % short_prime == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(StringContain('ABCD', 'BCD'))