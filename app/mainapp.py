#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
import math
from config import basedir


class MainApp:
    """
        This is a Main Application
    """
    def __init__(self, message, letters):
        self.message = message
        self.letters = letters

        # print(self.message)
        # print(self.letters)

    def hasmessage(self):
        # print(self.message)
        # print(self.letters)

        if self.message in self.letters:
            return True
        else:
            return False


if __name__ == '__main__':
    message = 'fkijdff'
    # letters = 'cvjolalgnfkdbooaslldfgDFGDFglsidjfokasdf'
    letters = 'fkijdff'

    print(message)
    print(letters)

    cooking = MainApp(message, letters)
    showme = cooking.hasmessage()

    print('My message is in the soup: {}'.format(showme))
