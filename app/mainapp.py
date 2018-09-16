#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
import math
from config import basedir
import cProfile, pstats


class MainApp:
    """
        This is a Main Application
        for Alphabet Soup Puzzle
    """
    def __init__(self, message, letters):
        self.message = message
        self.letters = letters

        # print(self.message)
        # print(self.letters)

    def has_message(self):
        # print(self.message)
        # print(self.letters)

        cleaned_message = self.clean_message()
        letters_in_bowl = self.clean_letters()

        method_1 = self.is_message_in_letters_method_1(cleaned_message, letters_in_bowl)
        method_2 = self.is_message_in_letters_method_2(cleaned_message, letters_in_bowl)
        method_3 = self.is_message_in_letters_method_3(cleaned_message, letters_in_bowl)

        return method_1, method_2, method_3

    def clean_string(self, input_string):
        """get rid of punctuation
        and create string of letters only
        """
        s = input_string
        print("s: {}".format(s))
        tokens = s.split()
        print("Original tokens: {}".format(tokens))

        new_tokens = []
        for token in tokens:
            # TODO: Add any punctuation you want get rid off
            token = token.strip('\'".,?:-!')
            print("token: {}".format(token))
            if token != '':
                new_tokens.append(token)

        new_string = ''.join(new_tokens)
        print("New tokens: {}".format(new_string))
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
        """DO NOT USE!
        Algoritmm method 1:
        Using membership feature -- very dirty! --
        exact sequence is required
        which is not the solution for the requested task
        E.g
        message = "Hello, World!"
        letters = 'startHelloWorldfoospamh'
        Use this method for quick work and testing template
        "Premature optimization is the root of al evil (or at least most of it)
        in programming" -- not my quote  :)
        """
        if message in letters:
            return True
        else:
            return False

    def is_message_in_letters_method_2(self, message, letters):
        """Algoritmm method 2:
        TODO Using membership -- cleaner
        needs to teste each messge item membership on letters in bowl
        """

        message_list = list(message)
        # for letter in message_list:


        if message in letters:
            return True
        else:
            return False

    def is_message_in_letters_method_3(self, message, letters):
        """Algoritmm method 3:
        TODO: Using list containers matching
        """
        if message in letters:
            return True
        else:
            return False


if __name__ == '__main__':
    # message = 'fkijdff'
    message = "Hello, World!"
    # letters = 'cvjolalgnfkdbooaslldfgDFGDFglsidjfokasdf'
    # letters = 'fkijdff'
    letters = 'startHelloWorldfoospamh'

    print(message)
    print(letters)

    cooking = MainApp(message, letters)
    # Using included profiler
    cProfile.run('cooking.has_message()', 'alphabetsoup.profile')
    p = pstats.Stats('alphabetsoup.profile')
    p.print_stats()

    show_me = cooking.has_message()

    print('My message is in the soup: {}'.format(show_me))
