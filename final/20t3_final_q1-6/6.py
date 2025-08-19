# COMP9021 20T3 - Rachid Hamadi
# Final Exam - Question 6

"""
by: ac_coder
"""
def search(grid, word, x, y):
    m, n = len(grid), len(grid[0])
    length = len(word)

    # Search whether the given word is in a row
    current_x, current_y, current_len = x, y, 0
    while current_x < m and current_len < length and grid[current_x][current_y] == word[current_len]:
        current_x += 1
        current_len += 1
    if current_len == length:
        return True

    # Search whether the given word is in a column
    current_x, current_y, current_len = x, y, 0
    while current_y < n and current_len < length and grid[current_x][current_y] == word[current_len]:
        current_y += 1
        current_len += 1
    if current_len == length:
        return True

    # Search whether the given word is in main diagonal
    current_x, current_y, current_len = x, y, 0
    while current_x < m and current_y < n and current_len < length and grid[current_x][current_y] == word[current_len]:
        current_x += 1
        current_y += 1
        current_len += 1
    if current_len == length:
        return True
    return False


def found_word_in(word, filename):
    '''
    Returns True or False depending on whether "word" can be read
    from the grid represented in the provided file "filename",
    assumed to be stored in the working directory.

    There can be spaces anywhere in the file. In particular,
    letters on a given line of the file can be separated by an
    arbitrary number of spaces (possibly none), and there can be
    lines with nothing but spaces.

    Words are to be read HORIZONTALLY FROM LEFT TO RIGHT,
    or VERTICALLY FROM TOP TO BOTTOM,
    or DIAGONALLY FROM TOP LEFT TO BOTTOM RIGHT


    >>> found_word_in('MANGANESE', 'word_search_1.txt'),\
        found_word_in('GOLD', 'word_search_1.txt')
    (True, False)
    >>> found_word_in('NICKEL', 'word_search_1.txt'),\
        found_word_in('SILVER', 'word_search_1.txt')
    (True, True)
    >>> found_word_in('ZINC', 'word_search_1.txt'),\
        found_word_in('RUBIS', 'word_search_1.txt')
    (True, False)
    >>> found_word_in('BANANA', 'word_search_2.txt'),\
        found_word_in('RASPBERRY', 'word_search_2.txt')
    (True, True)
    '''
    # Store grid data, i.e. a two-dimensional characters matrix
    grid = []
    with open(filename, "r") as f:
        # Read all rows
        raw_data = f.readlines()

        # Traverse every row
        for row in raw_data:
            # Filter left and right blank characters
            row = row.strip()

            # Filter empty rows
            if not row:
                continue

            # Get characters except whitespaces of current row, and add it to grid
            target = []
            for i in range(len(row)):
                if row[i] != " ":
                    target.append(row[i])
            grid.append(target)

    # Search whether the given word in grid on a row/column/main diagonal
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if search(grid, word, i, j):
                return True
    return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
