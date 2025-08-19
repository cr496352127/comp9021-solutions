"""
by: ac_coder
"""
def shape(nums):
    '''
    >>> shape([])
    >>> shape([5, 3, 2])
    x
    x
    x x
    x x x
    x x x
    >>> shape([0, 1, 3, 2, 4, 2, 0])
            x
        x   x
        x x x x
      x x x x x
    '''
    # Special case: list nums is empty, then output nothing
    if not nums:
        return

    # From the shape above, we can find that the height = max value in list nums, and width = length of list nums
    height, width = max(nums), len(nums)

    # Create a two-dimensional list to store characters in the shape above, by using list derivation
    result = [[""] * width for _ in range(height)]

    # Traverse every column first
    for y in range(width):
        # Then, traverse every row
        for x in range(height):
            # Calculate current height for x-th row
            current_height = height - x
            # If y-th column value is greater than or equal to current height, then fill a 'x'
            if nums[y] >= current_height:
                result[x][y] = "x"
            else:  # Otherwise, fill a whitespace
                result[x][y] = " "

    # Traverse every row of list result, and concat every character with a whitespace,
    # and strip the right whitespaces (if needed)
    for row in result:
        print(" ".join(row).rstrip())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
