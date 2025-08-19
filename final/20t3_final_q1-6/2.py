# Final Exam - Question 2

"""
by: ac_coder
"""
def filtered_sequence(L, n):
    '''
    Returns a list LL that keeps from L all elements e
    that are part of a sub-sequence of length at least n.

    All elements of the sub-sequence have the same value as e.

    You can assume that L is a list of valid integers.

    >>> filtered_sequence([], 2)
    []
    >>> filtered_sequence([7], 0)
    [7]
    >>> filtered_sequence([7], 1)
    [7]
    >>> filtered_sequence([7], 2)
    []
    >>> filtered_sequence([1, 3, 1, 2, 5, 6, 8, 2], 1)
    [1, 3, 1, 2, 5, 6, 8, 2]
    >>> filtered_sequence([1, 3, 3, 3, 2, 4, 4, 5, 6, 6, 6, 6], 2)
    [3, 3, 3, 4, 4, 6, 6, 6, 6]
    >>> filtered_sequence([7, 7, 7, 7, 2, 2, 7, 3, 4, 4, 4, 6, 5], 3)
    [7, 7, 7, 7, 4, 4, 4]
    >>> filtered_sequence([1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 5, 5, 5, 5, 5, 6], 4)
    [1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]
    '''

    LL = []
    # INSERT YOUR CODE HERE
    # If given list L is empty, then return L directly
    if not L:
        return LL

    length = len(L)
    # Use another variables:
    # current_elem: Mark current element to traverse
    # current_freq: Mark current frequency of current_elem
    # Initially, we start traversing from element at index 0, i.e. current_elem = L[0], current_freq = 1
    current_elem, current_freq = L[0], 1

    # Traverse rest elements
    for i in range(1, length):
        # L[i] is equal to current_elem, then add current_freq by 1
        if L[i] == current_elem:
            current_freq += 1
        else:  # Otherwise, we get a break index
            # If current_freq is greater than or equal to n, then we can add current_freq elems current_elem
            # to the result list LL
            if current_freq >= n:
                LL.extend([current_elem] * current_freq)

            # Update the new info of current_elem and current_freq by L[i] and 1 respectively
            current_elem, current_freq = L[i], 1

    # Finally, check current_freq again
    # If current_freq is greater than or equal to n, then we can add current_freq elems current_elem
    # to the result list LL
    if current_freq >= n:
        LL.extend([current_elem] * current_freq)
    return LL


if __name__ == '__main__':
    import doctest
    doctest.testmod()
