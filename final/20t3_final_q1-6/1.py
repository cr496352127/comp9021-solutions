# Final Exam - Question 1

"""
by: ac_coder
"""
def average_of_digits_common_to(*numbers):
    '''
    If there are no numbers, or if the numbers have no digits in common,
    then returns -1.
    Else, returns the average of the digits common to all numbers
    (each common digit being counted only once).

    You can assume that numbers are all valid non-negative integers.

    [KEYPOINT] Common digit: For a digit, it occurs in all of n numbers

    >>> average_of_digits_common_to()
    -1
    >>> average_of_digits_common_to(0, 12, 456)
    -1
    >>> average_of_digits_common_to(223444)\
#             (2 + 3 + 4) / 3 == 3.0
    3.0
    >>> average_of_digits_common_to(135, 567)\
#             5 / 1 == 5.0
    5.0
    >>> average_of_digits_common_to(234, 345, 2345, 3456, 112233445566)\
#             (3 + 4) / 2 == 3.5
    3.5
    >>> average_of_digits_common_to(932932, 139139, 395395395)\
#             (3 + 9) / 2 == 6.0
    6.0
    >>> average_of_digits_common_to(3136823, 665537857, 8363265, 35652385)\
#             (3 + 6 + 8) / 3 == 5.666666666666667
    5.666666666666667
    '''

    # Insert your code here
    # Transfer the given *numbers to a list
    numbers_list = list(numbers)

    # If numbers_list is empty, then return -1
    if not numbers_list:
        return -1

    # Maintain a dict, to store all indexes that 0-9 occurs
    # key: an integer digit, from 0 to 9
    # value: a list, that stores all indexes that 0-9 occurs
    digit_indexes = {}

    # Traverse every number in numbers_list, and count all indexes that 0-9 occurs
    n = len(numbers_list)
    for i in range(n):
        # A simpler solution: transfer current number to str
        num_str = str(numbers_list[i])

        # Use a set, to avoid duplication
        visited = set()

        # Traverse every character
        for digit in num_str:
            # If digit is existed in visited set, then skip it
            if digit in visited:
                continue

            # Otherwise, add it to visited
            visited.add(digit)

            # If digit is not in digit_indexes, then initialize corresponding value as a length=1 list
            if int(digit) not in digit_indexes:
                digit_indexes[int(digit)] = [i]
            else:
                digit_indexes[int(digit)].append(i)

    # Finally, find all common digits
    sum_of_common_digits, nb_of_common_digits = 0, 0
    for digit in range(10):
        # If the length of corresponding value (a list), of given digit in dict digit_indexes is n
        # then the digit is a common digit
        if digit in digit_indexes and len(digit_indexes[digit]) == n:
            sum_of_common_digits += digit
            nb_of_common_digits += 1

    # If nb_of_common_digits = 0, then no common digits existed
    if nb_of_common_digits == 0:
        return -1

    # Otherwise, return avg value (float type)
    return sum_of_common_digits / nb_of_common_digits


if __name__ == '__main__':
    import doctest

    doctest.testmod()
