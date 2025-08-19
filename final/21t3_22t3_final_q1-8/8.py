# COMP9021 22T3 - Rachid Hamadi
# Final Exam Question 8

def is_valid_values(square):
    """
    Check whether the values in given square are all valid
    i.e. the given square contains values from 1 to n**2 uniquely
    """
    n = len(square)
    visited = set()
    for i in range(n):
        for j in range(n):
            if square[i][j] < 1 or square[i][j] > n ** 2 or square[i][j] in visited:
                return False
            visited.add(square[i][j])
    return True


def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.

    Conjunctions of inputs will be tested, so hard coding will not help.

    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    # INSERT YOUR CODE HERE
    # If the square does not contain values from 1 to n**2 uniquely, then return False directly
    if not is_valid_values(square):
        return False

    # Maintain length (dimension) of given square
    n = len(square)

    # Maintain a set visited, to store visited sum
    visited = set()

    # Step 1. Traverse square, and calculate sum of every row
    for i in range(n):
        current_row_sum = 0
        for j in range(n):
            current_row_sum += square[i][j]

        # If current_row_sum is in visited, then return False directly
        # Otherwise, add it to visited
        if current_row_sum in visited:
            return False
        visited.add(current_row_sum)

    # Step 2. Traverse square, and calculate sum of every column
    for j in range(n):
        current_column_sum = 0
        for i in range(n):
            current_column_sum += square[i][j]

        # If current_col_sum is in visited, then return False directly
        # Otherwise, add it to visited
        if current_column_sum in visited:
            return False
        visited.add(current_column_sum)

    # Step 3. Traverse square, and calculate sum of main diagonal
    current_main_diag_sum = 0
    for i in range(n):
        current_main_diag_sum += square[i][i]

    # If current_main_diag_sum is in visited, then return False directly
    # Otherwise, add it to visited
    if current_main_diag_sum in visited:
        return False
    visited.add(current_main_diag_sum)

    # Step 4. Traverse square, and calculate sum of sub diagonal
    current_sub_diag_sum = 0
    for i in range(n):
        current_sub_diag_sum += square[i][n - 1 - i]

    # If current_sub_diag_sum is in visited, then return False directly
    # Otherwise, we can find that the given square is a heterosquare, then return True
    if current_sub_diag_sum in visited:
        return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
