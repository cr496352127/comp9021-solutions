# COMP9021 21T3 - Rachid Hamadi
# Final Exam Question 3

'''
You might find the ord() function useful.
'''


def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    Find and return the LONGEST LEFTMOST sequence of consecutive letters.
    You can assume that "word" is a string of nothing but lowercase letters.

    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwrstuvabcde')
    'rstuv'
    '''
    # INSERT YOUR CODE HERE
    # If the given word is empty, then return it directly
    if not word:
        return ""

    n = len(word)

    # Store current_str that has leftmost sequence of consecutive letters
    # Initially, the character at index 0 must in current_str
    current_str = word[0]

    # Store the result. It can be initialized by current_str above
    res = current_str

    # Traverse another characters from index 1
    for i in range(1, n):
        # Store ord value of prev character (prev_ord) and current character (current_ord) respectively
        prev_ord, current_ord = ord(word[i - 1]), ord(word[i])

        # If current_ord is greater than prev_ord by 1, then we can add character word[i] to current_str
        if current_ord == prev_ord + 1:
            current_str += word[i]

        # Otherwise, we get a break index
        else:
            # If length of current_str is greater than that of res, then we set res = current_str
            if len(current_str) > len(res):
                res = current_str

            # Regardless of the above if statement is true, we should set current_word = word[i], to find new current_str
            current_str = word[i]

    # Finally, we should check again, because current_str after traversing may have longer length than that of res
    if len(current_str) > len(res):
        res = current_str
    return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
