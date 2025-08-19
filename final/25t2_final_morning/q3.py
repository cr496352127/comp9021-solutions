"""
by: ac_coder
"""
def dfs(number_str, product, current_index, current_seq, current_prod):
    """
    Search by using recursion (depth first search)
    :param number_str: string representation of given number
    :param product: Target multiple
    :param current_index: Current index (start from 0, and end to len(number_str))
    :param current_seq: Current selected digits
    :param current_prod: Current product of selected digits (from 0 to 9)
    :return: None (Results will be stored into list result)
    """
    # Base case: All digits are traversed
    if current_index == len(number_str):
        # If current_prod is equal to product, then add integer representation of current_seq
        if current_prod == product:
            global result
            result.append(int(current_seq))
        return

    # Recursive function:
    # Case 1. Select digit at current_index, then update current_index, current_seq and current_prod
    digit = int(number_str[current_index])
    if str(digit) not in current_seq:
        dfs(number_str, product, current_index + 1, current_seq + number_str[current_index], current_prod * digit)

    # Case 2. Do not select digit at current_index, then only update current_index
    dfs(number_str, product, current_index + 1, current_seq, current_prod)


def target_product(number, target):
    '''
    >>> target_product(12234612, 24)
    [46, 146, 234, 234, 342, 461, 1234, 1234, 1342, 2341, 2341, 3412]
    '''
    # Define a global variable list, to store the result integers
    global result; result = []

    # Search by using recursion (depth first search)
    dfs(str(number), target, 0, "", 1)

    # Finally, sort the result containing target integers in ascending order (if needed)
    return sorted(result)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
