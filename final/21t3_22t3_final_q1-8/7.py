# COMP9021 21T3 - Rachid Hamadi
# Final Exam Question 7

from random import seed, randrange
from collections import deque


def area(for_seed, sparsity, i, j):
    '''
    Find the area of the largest empty region of the 10 * 10 grid containing the point (i, j).
    You can assume that i and j are both between 0 and 9 included.
    i is the row number (indexed from top to bottom),
    j is the column number (indexed from left to right)
    of the displayed grid.

    >>> area(0, 1, 5, 5)
    The grid is:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    The area of the largest empty region of the grid
    containing the point (5, 5) is: 0
    >>> area(0, 1000, 5, 5)
    The grid is:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    The area of the largest empty region of the grid
    containing the point (5, 5) is: 100
    >>> area(0, 3, 6, 2)
    The grid is:
    0 0 1 0 0 0 0 0 0 0
    0 1 0 1 0 1 1 0 0 0
    0 0 1 0 1 0 1 0 0 0
    0 1 0 0 0 0 0 1 0 0
    0 0 0 1 0 1 1 0 0 0
    0 0 1 0 0 0 1 0 0 0
    1 1 0 1 1 1 0 0 1 1
    0 0 0 1 0 0 0 0 1 0
    0 0 1 0 0 0 0 0 1 0
    0 0 0 1 0 1 1 1 1 0
    The area of the largest empty region of the grid
    containing the point (6, 2) is: 9
    >>> area(0, 2, 9, 5)
    The grid is:
    0 0 1 0 0 0 0 0 0 1
    1 0 1 1 0 1 0 1 1 0
    0 1 0 0 0 1 0 0 0 1
    1 1 0 1 0 0 1 0 1 1
    1 1 1 0 1 1 0 0 1 0
    0 1 0 1 0 0 1 0 0 1
    0 1 1 1 1 0 0 1 1 1
    1 1 1 0 0 1 1 0 0 0
    0 0 1 0 1 0 0 1 1 1
    0 1 1 0 1 0 0 1 1 1
    The area of the largest empty region of the grid
    containing the point (9, 5) is: 4
    >>> area(0, 2, 2, 7)
    The grid is:
    0 0 1 0 0 0 0 0 0 1
    1 0 1 1 0 1 0 1 1 0
    0 1 0 0 0 1 0 0 0 1
    1 1 0 1 0 0 1 0 1 1
    1 1 1 0 1 1 0 0 1 0
    0 1 0 1 0 0 1 0 0 1
    0 1 1 1 1 0 0 1 1 1
    1 1 1 0 0 1 1 0 0 0
    0 0 1 0 1 0 0 1 1 1
    0 1 1 0 1 0 0 1 1 1
    The area of the largest empty region of the grid
    containing the point (2, 7) is: 22
    >>> area(0, 4, 2, 7)
    The grid is:
    0 0 1 0 0 0 0 0 0 0
    0 0 0 1 0 0 0 1 1 0
    0 1 0 0 0 0 0 0 0 1
    1 1 0 1 0 0 0 0 1 0
    0 0 0 0 1 1 0 0 1 0
    0 1 0 0 0 0 1 0 0 0
    0 0 0 0 1 0 0 1 1 0
    0 1 1 0 0 0 0 0 0 0
    0 0 1 0 1 0 0 0 0 1
    0 1 0 0 0 0 0 1 1 0
    The area of the largest empty region of the grid
    containing the point (2, 7) is: 73
    '''

    seed(for_seed)
    grid = [[int(randrange(sparsity) == 0) for _ in range(10)] for _ in range(10)]
    print('The grid is:')
    for row in grid:
        print(*row)

    # ADD YOUR CODE HERE (A PRINT STATEMENT AT THE END IS NEEDED)
    # Use a variable area to store the largest area (containing the start position)
    area = 1

    # (i, j) is not a valid start position
    if grid[i][j] != 0:
        area = 0
    else:
        # Add the given start position (i, j) into the queue
        que = deque([[i, j]])

        # Mark (i, j) is visited (1), in order to avoid return (i, j) again
        grid[i][j] = 1

        # Use a list to record all candidate moving directions
        # UP: (x, y) -> (x - 1, y)
        # DOWN: (x, y) -> (x + 1, y)
        # LEFT: (x, y) -> (x, y - 1)
        # RIGHT: (x, y) -> (x, y + 1)
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # If the given que is not empty, then circulate
        while que:
            # Fetch and pop the front element (i.e. front position)
            current_i, current_j = que.popleft()

            # Move: (current_i, current_j) -> (next_i, next_j)
            for k in range(len(dirs)):
                next_i = current_i + dirs[k][0]
                next_j = current_j + dirs[k][1]

                # Check validation of (next_i, next_j)
                # 1. Inside: 0 <= next_i < 10 and 0 <= next_j < 10
                # 2. grid[next_i][next_j] == 0, i.e. (next_i, next_j) has not been visited (0)
                if 0 <= next_i < 10 and 0 <= next_j < 10 and grid[next_i][next_j] == 0:
                    # Add (next_i, next_j) to que
                    que.append([next_i, next_j])

                    # Mark (next_i, next_j) is visited (1)
                    grid[next_i][next_j] = 1

                    # Update area
                    area += 1

    print("The area of the largest empty region of the grid")
    print("containing the point ({}, {}) is: {}".format(i, j, area))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
