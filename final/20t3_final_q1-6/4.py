# Final Exam - Question 4

"""
by: ac_coder
"""
def subnumbers_whose_digits_add_up_to(number, sum_of_digits):
    '''
    You can assume that "number" consists of digits not equal to 0
    and that "sum_of_digits" is a strictly positive integer.

    A solution is obtained by possibly deleting some digits in "number"
    (keeping the order of the remaining digits)
    => For every digit in "number", we can: <select> or <not select>

    so that the sum of
    the remaining digits is equal to "sum_of_digits".

    The solutions are listed from smallest to largest, with no duplicate.
    => Return a <list>

    >>> subnumbers_whose_digits_add_up_to(13, 2)
    []
    >>> subnumbers_whose_digits_add_up_to(222, 2)
    [2]
    >>> subnumbers_whose_digits_add_up_to(123, 6)
    [123]
    >>> subnumbers_whose_digits_add_up_to(222, 4)
    [22]
    >>> subnumbers_whose_digits_add_up_to(1234, 5)
    [14, 23]
    >>> subnumbers_whose_digits_add_up_to(12341234, 4)
    [4, 13, 22, 31, 112, 121]
    >>> subnumbers_whose_digits_add_up_to(121212, 5)
    [122, 212, 221, 1112, 1121, 1211]
    >>> subnumbers_whose_digits_add_up_to(123454321, 10)
    [145, 154, 235, 244, 253, 343, 352, 442, 451, 532, 541, 1234, 1243, \
1252, 1342, 1351, 1432, 1441, 1531, 2332, 2341, 2431, 2521, 3421, \
4321, 12331, 12421, 13321]
    '''
    # REPLACE "pass" ABOVE WITH YOUR CODE
    # We can use "global" keyword, to define variables that can be used in other functions
    global result
    result = []

    # Call helper function
    subnumbers_helper(str(number), sum_of_digits, "", 0)

    # Finally, sort and remove duplicates, and return the result
    # # Step 1. Remove duplicates by using set
    # result_set = set(result)
    #
    # # Step 2. Turn to list again, and sort it
    # result_list = list(result_set)
    # result_list.sort()
    #
    # # Step 3. Return the sorted result_list
    # return result_list
    result_list = list(set(result))
    result_list.sort()
    return result_list


# POSSIBLY DEFINE OTHER FUNCTIONS
def subnumbers_helper(number_str, sum_of_digits, selected_digits, selected_sum_of_digits):
    # Base case: number_str is empty, check whether selected_sum_of_digits is equal to sum_of_digits
    # If True, then we can add selected_digits to result
    if number_str == "":
        if selected_sum_of_digits == sum_of_digits:
            # Add the integer representation of selected_digits to result
            global result
            result.append(int(selected_digits))
        return

    current_digit = number_str[0]  # str
    next_number_str = number_str[1:]  # str slice

    # Case 1. Select current_digit
    subnumbers_helper(next_number_str, sum_of_digits, selected_digits + current_digit, selected_sum_of_digits + int(current_digit))

    # Case 2. Not select current digit
    subnumbers_helper(next_number_str, sum_of_digits, selected_digits, selected_sum_of_digits)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
