#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter
import cProfile, pstats


class MainApp:
    """This is a Main Application  for Alphabet Soup Puzzle
    Steps overview:
    1. We do a cleaning process getting rid of punctuations and leaving only letters (or numbers) in the input strings.
    2. Apply the matching method on the strings
    3. Strings are converted into Multi-Sets
    4. Reuse Multi-Sets capabilities (in Python -- similar to a pseudo-code --)
    for matching the existence of each element from "message to write" into "the bowl with alphabet soup"
    5. Returning True if the letters in message exist in the alphabet bowl, otherwise return False.

    Big-O Notation / Analysis: (Which one is the most representative?)
    (A) O(n)
    (B) O(n^2)
    (C) O(log n)
    (D) O(n^3)

    - Function "is_message_in_letters_method_1"  implements a Compare method of two Multi-Sets,
    in the way its elements can be duplicated and unordered.
    - The two input strings are not the same length (m,s).
    - In the main internal matching cycle, the function immediately interrupts
    processing and returns False, in case there is an element in message with no matching in the bowl,
    avoiding processing the whole message.
    - The worst scenario is when all the message letters are included in the alphabet bowl.
    - The method is practically based on the frequency of the items in the bowl.
    - For for Big-O running time there is considered one big cycle to run through two possible variables:
        - length of the message (m) and
        - the number of letters in the bowl of soup (s)
    - The solution has a number of iterations, none of them is nested.
    - The Big-O running time is of:
        --   O(ms)
    """
    def __init__(self, message, letters):
        self.message = message
        self.letters = letters

    def has_message(self):
        cleaned_message = self.clean_message()
        letters_in_bowl = self.clean_letters()

        method_1 = self.is_message_in_letters_method_1(cleaned_message, letters_in_bowl)

        return method_1

    def clean_string(self, input_string):
        """get rid of punctuation
        and create string of letters only
        """
        s = input_string
        tokens = s.split()

        new_tokens = []
        for token in tokens:
            # TODO: Add any punctuation you want get rid off
            token = token.strip('\'".,?:-!')
            if token != '':
                new_tokens.append(token)

        new_string = ''.join(new_tokens)
        return new_string

    def clean_message(self):
        """get rid of punctuation
        and create string of letters only
        on message to write
        """
        return self.clean_string(self.message)

    def clean_letters(self):
        """get rid of punctuation
        and create string of letters only
        on letters in bowl
        """
        return self.clean_string(self.letters)

    def is_message_in_letters_method_1(self, message, letters):
        """Algorithm method 1:
        Using containers (collections.Counter class) matching
        subtract([iterable-or-mapping])
        Elements are subtracted from an iterable or from another mapping (or counter). Like dict.update()
        but subtracts counts instead of replacing them. Both inputs and outputs may be zero or negative.
        >>> c = Counter(a=4, b=2, c=0, d=-2)
        >>> d = Counter(a=1, b=2, c=3, d=4)
        >>> c.subtract(d)
        >>> c
        Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
        """
        print("Message lengh: {}".format(len(message)))
        print("Number of letters: {}".format(len(letters)))
        message_c = Counter(message)
        letters_c = Counter(letters)
        letters_c.subtract(message_c)
        for letter in message_c.elements():
            if letters_c[letter] < 0:
                return False
        return True


if __name__ == '__main__':
    # message = 'fkijdff'
    # message = "Hello, World!"
    # letters = 'cvjolalgnfkdbooaslldfgDFGDFglsidjfokasdf'
    # letters = 'fkijdff'
    # letters = 'startHelloWorldfoospamh'
    message = "HelloWorldHH"
    letters = 'startHeoWordfoospamHh'

    cooking = MainApp(message, letters)
    # Using included profiler
    cProfile.run('cooking.has_message()', 'alphabetsoup.profile')
    p = pstats.Stats('alphabetsoup.profile')
    p.print_stats()

    show_me = cooking.has_message()

    print('My message is in the soup: {}'.format(show_me))
