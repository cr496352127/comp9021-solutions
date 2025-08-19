# COMP9021 22T3 - Rachid Hamadi
# Final Exam Question 6

def statistics(filename):
    '''
    A text file, stored in the working directory, consists of sentences.
    A sentence consists of words, possibly directly followed by a comma,
    except for the last word which is directly followed by a full stop.
    Words are separated by spaces.

    >>> statistics('text_file_1.txt')
    There are 2 sentence(s).
    The shortest sentence has 31 word(s).
    The longest sentence has 34 word(s).
    The shortest word has 1 character(s).
    The longest word has 9 character(s).
    >>> statistics('text_file_2.txt')
    There are 4 sentence(s).
    The shortest sentence has 6 word(s).
    The longest sentence has 34 word(s).
    The shortest word has 1 character(s).
    The longest word has 12 character(s).
    >>> statistics('text_file_3.txt')
    There are 1 sentence(s).
    The shortest sentence has 30 word(s).
    The longest sentence has 30 word(s).
    The shortest word has 1 character(s).
    The longest word has 12 character(s).
    '''

    nb_of_sentences = None
    length_of_shortest_word = None
    length_of_longest_word = None
    min_nb_of_words_in_sentences = None
    max_nb_of_words_in_sentences = None

    with open(filename) as file:
        # Read all characters as a str
        raw_data_str = file.read().strip()
        # print(raw_data_str)

        # Split the raw_data_str by '.', and get number of sentences
        sentences = raw_data_str.split('.')[:-1]
        nb_of_sentences = len(sentences)

        # Replace '\n' with a whitespace ' '
        for sentence in sentences:
            sentence = sentence.replace('\n', ' ').strip()

            # Split every sentence by ' ' (considering multiple whitespaces may existed, then we can use split() directly)
            words = sentence.split()

            # Calculate the number of words of current sentence, and maintain the min and max values
            nb_of_words = len(words)
            if not min_nb_of_words_in_sentences or nb_of_words < min_nb_of_words_in_sentences:
                min_nb_of_words_in_sentences = nb_of_words
            if not max_nb_of_words_in_sentences or nb_of_words > max_nb_of_words_in_sentences:
                max_nb_of_words_in_sentences = nb_of_words

            # Traverse every word
            for word in words:
                if word and word[-1] == ',':
                    word = word[:-1]
                # Calculate the number of characters of current word, and maintain the min and max values
                nb_of_characters = len(word)
                if not length_of_shortest_word or nb_of_characters < length_of_shortest_word:
                    length_of_shortest_word = nb_of_characters
                if not length_of_longest_word or nb_of_characters > length_of_longest_word:
                    length_of_longest_word = nb_of_characters

    print('There are', nb_of_sentences, 'sentence(s).')
    print('The shortest sentence has', min_nb_of_words_in_sentences, 'word(s).')
    print('The longest sentence has', max_nb_of_words_in_sentences, 'word(s).')
    print('The shortest word has', length_of_shortest_word, 'character(s).')
    print('The longest word has', length_of_longest_word, 'character(s).')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
