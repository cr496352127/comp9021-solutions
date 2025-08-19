# COMP9021 21T3 - Rachid Hamadi
# Final Exam Question 5
from math import sqrt


def get_sum_of_proper_divisors(num):
    if num <= 0:
        return 0

    factor_sum = 0
    for factor1 in range(1, int(sqrt(num)) + 1):
        if num % factor1 == 0:
            factor_sum += factor1

            factor2 = num // factor1
            if num % factor2 == 0 and factor2 != factor1 and factor2 != num:
                factor_sum += factor2
    return factor_sum


def betrothed_pair(n):
    '''
    A pair of natural numbers (m, n) is a BETROTHED PAIR if:
    - the sum of the proper divisors of n is one more than m (sum of factors in n = m + 1);
    - the sum of the proper divisors of m is one more than n (sum of factors in m = n + 1).
    For instance, (48, 75) is a Betrothed pair since
    - the proper divisors of 48 are 1, 2, 3, 4, 6, 8, 12, 16 and 24
    - the proper divisors of 75 are 1, 3, 5, 15 and 25
    - 1 + 2 + 3 + 4 + 6 + 8 + 12 + 16 + 24 = 76
    - 1 + 3 + 5 + 15 + 25 = 49

    You can assume that n is an integer at least equal to 0.
    Will not be tested for n greater than 10_000.

    >>> betrothed_pair(0)
    The least number >= 0 that is the first member of a Betrothed pair is 48
    The Betrothed itself is (48, 75)
    >>> betrothed_pair(50)
    The least number >= 50 that is the first member of a Betrothed pair is 75
    The Betrothed itself is (75, 48)
    >>> betrothed_pair(100)
    The least number >= 100 that is the first member of a Betrothed pair is 140
    The Betrothed itself is (140, 195)
    >>> betrothed_pair(1000)
    The least number >= 1000 that is the first member of a Betrothed pair is 1050
    The Betrothed itself is (1050, 1925)
    >>> betrothed_pair(10000)
    The least number >= 10000 that is the first member of a Betrothed pair is 16587
    The Betrothed itself is (16587, 8892)
    '''
    a = n
    while True:
        sum_a = get_sum_of_proper_divisors(a)
        b = sum_a - 1
        sum_b = get_sum_of_proper_divisors(b)

        if sum_b == a + 1:
            print("The least number >= {} that is the first member of a Betrothed pair is {}".format(n, a))
            print("The Betrothed itself is ({}, {})".format(a, b))
            break
        else:
            a += 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
