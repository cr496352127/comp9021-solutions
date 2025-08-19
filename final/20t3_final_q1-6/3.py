# Final Exam - Question 3

# ord(c) returns the encoding (ASCII encoding) of character c.
# chr(e) returns the character encoded by e.



"""
by: ac_coder

Every character of rectangle is lowercases between 'a' and 'z'
1. Number of rectangle rows = height, columns = width
2. Number of rectangle rows and columns are constant, but:
    1) For odd i-th (1, 3, 5, ...) row, the lowercases are arranged from left to right
    2) For even i-th (2, 4, 6, ...) row, the lowercases are arranged from right to left
3. 'a' -> 'b' -> ... -> 'y' -> 'z' -> 'a' -> 'b' -> ...
    For current character ord(ch), then the next character is ord(ch) + 1
"""
def f(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when
    z is reached.

    You can assume that width and height are strictly positive integers

    >>> f(1, 1)
    a
    >>> f(2, 3)
    ab
    dc
    ef
    >>> f(3, 2)
    abc
    fed
    >>> f(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''

    # INSERT YOUR CODE HERE
    # Define an integer to store current character's ord value
    current_ord = ord("a")  # 97

    for i in range(1, height + 1):
        # Define current row to be outputted
        row = ""

        for j in range(1, width + 1):
            # Transfer current_ord to corresponding character, and add it to the tail of row
            row += chr(current_ord)

            # If current character is "z", then the next character to be outputted is "a"
            if chr(current_ord) == "z":
                current_ord = ord("a")
            else:  # Otherwise, the next character is after it
                current_ord += 1

        # Output current i-th row
        # We can use slice to control the direction
        if i % 2 == 1:
            print(row)
        else:  # Use row[::-1] to change the direction
            print(row[::-1])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
