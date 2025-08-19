# COMP9021 21T3 - Rachid Hamadi
# Final Exam Question 1

def count_of_given_digit_in_numbers_in_list(L, d):
    '''
    Count and return the number of given digit (SINGLE DIGIT) d in the given list L.
    You can assume that L is a list of positive integers and d is a digit.

    >>> count_of_given_digit_in_numbers_in_list([3, 3333, 33], 3)
    7
    >>> count_of_given_digit_in_numbers_in_list([13, 14, 258], 9)
    0
    >>> count_of_given_digit_in_numbers_in_list([1, 21, 30, 1411], 1)
    5
    >>> count_of_given_digit_in_numbers_in_list([4082, 5395, 7888, 5697], 0)
    1
    >>> count_of_given_digit_in_numbers_in_list([4082, 5395, 7888, 5697], 1)
    0
    >>> count_of_given_digit_in_numbers_in_list([4082, 5395, 7888, 5697], 7)
    2
    >>> count_of_given_digit_in_numbers_in_list([4082, 5395, 7888, 5697], 8)
    4
    '''
    # Transfer the given digit d to str
    str_d = str(d)

    # Count sum of occurrence of d in L
    result = 0

    for num in L:
        result += str(num).count(str_d)
    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
