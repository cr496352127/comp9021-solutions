# COMP9021 21T3 - Rachid Hamadi
# Final Exam Question 4

'''
No point to hard code for small values of n, will be tested
only for large enough values...
'''


def pascal_triangle_line(n):
    '''
    Return the n-th line of pascal triangle.
    Hint: The structure of pascal triangle is shown as follows:
    1
    1  1
    1  2  1
    1  3  3   1
    1  4  6   4   1
    1  5  10  10  5   1
    1  6  15  20  15  6   1
    1  7  21  35  35  21  7  1

    We can find that:
    1) Values at first column are always 1
    2) Values at the main diagonal are always 1
    3) Values at other positions (x, y) are sum of values at position (x - 1, y - 1) and (x - 1, y)

    Recall: it is the list of binomial coefficients that give the
    number of ways of choosing k objects out of n - 1 for 0 <= k < n.

    >>> pascal_triangle_line(1)
    [1]
    >>> pascal_triangle_line(2)
    [1, 1]
    >>> pascal_triangle_line(3)
    [1, 2, 1]
    >>> pascal_triangle_line(4)
    [1, 3, 3, 1]
    >>> pascal_triangle_line(5)
    [1, 4, 6, 4, 1]
    >>> pascal_triangle_line(6)
    [1, 5, 10, 10, 5, 1]
    >>> pascal_triangle_line(7)
    [1, 6, 15, 20, 15, 6, 1]
    >>> pascal_triangle_line(8)
    [1, 7, 21, 35, 35, 21, 7, 1]
    '''
    # INSERT YOUR CODE HERE
    # Define a two-dimensional list res
    # res[i][j]: value of pascal triangle value at i-th row and j-th column
    res = [[0] * n for _ in range(n)]

    # Considering the value distribution above, we can find that:
    # 1. When i = 0 (the 0-th column), or j = i (the main diagonal), then the value is always 1
    for i in range(n):
        res[i][0] = 1
        res[i][i] = 1

    # 2. Otherwise, values at i-th row and j-th column are always:
    # value at (i - 1)-th row and (j - 1)-th column PLUS
    # value at (i - 1)-th row and j-th column
    # i.e. res[i][j] = res[i - 1][j - 1] + res[i - 1][j] (1 <= i < n, 1 <= j < i)
    for i in range(1, n):
        for j in range(1, i):
            res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

    # Finally, res[n - 1] contains values of pascal triangle at (n - 1)-th row
    return res[n - 1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
