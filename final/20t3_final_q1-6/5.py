# Final Exam - Question 5

"""
by: ac_coder
"""
dictionary_file = 'dictionary.txt'


def number_of_words_in_dictionary(word1, word2):
    '''
    Determines the number of words BETWEEN two words "word1"
	AND "word2" INCLUSIVE in the provided "dictionary.txt".

    "dictionary.txt" is stored in the working directory.
    Words in "dictionary.txt" are all uppercase.
    Words are CASE SENSITIVE.


    >>> number_of_words_in_dictionary('company', 'company')
    Could not find company in dictionary.
    >>> number_of_words_in_dictionary('company', 'comparison')
    Could not find at least one of company and comparison in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'comparison')
    Could not find at least one of COMPANY and comparison in dictionary.
    >>> number_of_words_in_dictionary('company', 'COMPARISON')
    Could not find at least one of company and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPANY')
    COMPANY is in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPARISON')
    COMPARISON is in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPARISON')
    Found 14 words between COMPANY and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPANY')
    Found 14 words between COMPARISON and COMPANY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIOUSLY')
    Found 2 words between CONSCIOUS and CONSCIOUSLY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIENTIOUS')
    Found 3 words between CONSCIOUS and CONSCIENTIOUS in dictionary.
    '''
    # Open the given dictionary file
    with open(dictionary_file, "r") as f:
        # Read all words in the given dictionary file
        raw_data = f.readlines()

        # Maintain two indexes to record the occurrence of given two words
        # Initially, we suppose they are not existed
        word1_index, word2_index = None, None

        # Traverse all words with indexes
        n = len(raw_data)
        for i in range(n):
            # Filter the '\n' character, and get current word
            current_word = raw_data[i].strip()

            # Check whether current_word is word1, or word2
            if current_word == word1:
                word1_index = i
            if current_word == word2:
                word2_index = i

        # Case 1. Could not find word => word1 = word2, or word1 != word2
        if not word1_index or not word2_index:
            if word1 == word2:
                print("Could not find {} in dictionary.".format(word1))
            else:
                print("Could not find at least one of {} and {} in dictionary.".format(word1, word2))

        # Case 2. Could find word => word1 = word2, or word1 != word2
        else:  # Equal to word1_index and word2_index both are not None
            if word1 == word2:
                print("{} is in dictionary.".format(word1))
            else:
                amount = abs(word1_index - word2_index) + 1
                print("Found {} words between {} and {} in dictionary.".format(amount, word1, word2))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
