"""
******************************************************************
@Title: 合法字符串
@Method: 1. 记满足2i > n的字符个数为s；
         2. 当n为偶数时，满足2i > n的字符个数s = 1/2 * n；
         3. 当n为奇数时，满足2i > n的字符个数s = 1/2 * n + 1；
         4. 记满足2i <= n的字符个数为t；
         5. 则当n为偶数时，t = n - 1/2 * n；当n为奇数时，t = n - 1/2 * n - 1；
         6. 记可分配满足2i <= n的字符的位置数为k；
         7. 当m-1为偶数时，k = 1/2 * (m-1)；当m-1为奇数时，k = 1/2 * (m-1) + 1；
         8. 合法字符串数为：s * (s**(m-1) + C(1, m-1)*s**(m-2)*t + ... + (C(k, m-1) - (m - k))*s**(m-1-k)*t**k)；
******************************************************************
"""


def Cmn(n, m):

    if m == 0:
        return 1
    else:
        numerator = 1
        for i in range(n-m+1, n+1):
            numerator *= i
        denominator = 1
        for j in range(1, n-m+1):
            denominator *= j

        return numerator / denominator


def legalSting(n, m):

    # Compute the number of characters that satisfy 2i > n condition
    if n % 2 == 0:
        s = int(1/2 * n)
    else:
        s = int(1/2 * n) + 1

    # Compute the number of characters that satisfy 2i <= n condition
    t = n - s

    # Compute the number of position that can be allocated to chars of satisfy 2i <= n
    if (m-1) % 2 == 0:
        k = int(1/2 * (m - 1))
    else:
        k = int(1/2 * (m - 1)) + 1

    # Compute the number of legal characters
    count = 0
    for i in range(0, k+1):
        if i < 2:
            count += Cmn(n, i) * s ** (m-1-i) * t ** i
        else:
            count += (Cmn(n, i) - (m-i)) * s ** (m-1-i) * t ** i

    return int(s * count)


if __name__ == "__main__":
    print(legalSting(3, 3))