"""
Special hint: Equal to LeetCode 54
by: ac_coder
"""
def update_ord(current_ord):
    """
    Update value of current ord
    """
    # If current_ord is equal to ord("z"), then set it by ord("a")
    if current_ord == ord("z"):
        return ord("a")

    # Otherwise, add it by 1
    return current_ord + 1


def f(w, h):
    '''
    >>> f(5, 3)
    abcde
    lmnof
    kjihg
    '''
    # Based on the rule of the circular matrix, we set:
    # (current_x, current_y): current position to fill lowercase character
    # current_ord: current ord value of lowercase character
    current_x, current_y, current_ord = 0, 0, ord("a")

    # filled_amount: Number of lowercase characters that have been filled
    filled_amount = 0

    # Create a two-dimensional list with h rows and w columns, to store the circular matrix by using list derivation
    result = [[""] * w for _ in range(h)]

    # If filled_amount is lower than h * w, then fill the circular matrix
    while filled_amount < h * w:
        # Fill in the horizontal direction from left to right,
        # until current_y is equal to w, or position (current_x, current_y) has been filled
        while current_y < w and result[current_x][current_y] == "":
            result[current_x][current_y] = chr(current_ord)
            filled_amount += 1
            current_ord = update_ord(current_ord)
            current_y += 1
        # Important: Adjust position (current_x, current_y), same as below
        current_y -= 1; current_x += 1

        # Fill in the vertical direction from up to down,
        # until current_x is equal to h, or position (current_x, current_y) has been filled
        while current_x < h and result[current_x][current_y] == "":
            result[current_x][current_y] = chr(current_ord)
            filled_amount += 1
            current_ord = update_ord(current_ord)
            current_x += 1
        current_x -= 1; current_y -= 1

        # Fill in the horizontal direction from right to left,
        # until current_y is equal to -1, or position (current_x, current_y) has been filled
        while current_y >= 0 and result[current_x][current_y] == "":
            result[current_x][current_y] = chr(current_ord)
            filled_amount += 1
            current_ord = update_ord(current_ord)
            current_y -= 1
        current_y += 1; current_x -= 1

        # Fill in the vertical direction from down to up,
        # until current_x is equal to -1, or position (current_x, current_y) has been filled
        while current_x >= 0 and result[current_x][current_y] == "":
            result[current_x][current_y] = chr(current_ord)
            filled_amount += 1
            current_ord = update_ord(current_ord)
            current_x -= 1
        current_x += 1; current_y += 1

    # Traverse every row of list result, and concat every character with a whitespace
    for row in result:
        print("".join(row))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
