#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Alphabet soup

Everyone loves alphabet soup.  And of course,
you want to know if you can construct a message
from the letters found in your bowl.

Your Task:

Write a function that takes as input two strings:
1. the message you want to write
2. all the letters found in your bowl of alphabet soup.

Assumptions:
- It may be a very large bowl of soup containing many letters.
- There is no guarantee that each letter occurs a similar number of times -
indeed some letters might be missing entirely.
- The letters are ordered randomly.

The function should determine if you can write your message with the letters
found in your bowl of soup. The function should return True or False
accordingly.

Try to make your function efficient.  Please use Big-O notation to explain how
long it takes your function to run in terms of the length of your message (m)
and the number of letters in your bowl of soup (s).

====================

Created 1 algorithm and adapted other 2 algorithms copied from
anagram implementation.
Pending to adapt a 4th algorithm based in ord('!') function
"""

from collections import Counter
import cProfile, pstats
import os, sys
import codecs


def etime():
    """See how much user and system time this process has used
    so far and return the sum.

    To measure the elapsed time of a function you can call etime twice and compute the difference:
    start = etime()
    # put the code you want to measure here
    end = etime()
    elapsed = end - start
    """
    user, sys, chuser, chsys, real = os.times()
    return user+sys


class MainApp:
    """This is a Main Application  for Alphabet Soup Puzzle
    Steps overview:
    1. We do a cleaning process getting rid of punctuations and leaving only
     letters (or numbers) in the input strings.
    2. Apply the matching method on the strings
    3a. Method 1: Strings are converted into Multi-Sets.
    Reuse Multi-Sets capabilities (in Python -- similar to a pseudo-code --)
    for matching the existence of each element from "message to write" into
    "the bowl with alphabet soup"
    3b. Method 2: Similar as Anagram implementation - Checking Off
    3c. Method 3: Similar as Anagram Implementation - Sort and Compare
    3d. DO NOT USE!!!  Attempt to use Anagram Implementation - Count and Compare
    4. Returning True if the letters in message exist in the alphabet bowl,
    otherwise return False.

    Big-O Notation / Analysis: (Which one is the most representative?)
    (A) O(n)
    (B) O(n^2)
    (C) O(log n)
    (D) O(n^3)

    - See each function comment for details of implemented methods
    e.g. "is_message_in_letters_method_1"  implements a Compare method
    of two Multi-Sets, in the way its elements can be duplicated and unordered.
    - See the attached AlphabetSoutpBig-O.xlsx file for more details

    - Computer: i7 1.8GHz
       Filesystem: on HDD


    - TODO: Needed to test with hyper-big input data for message length.
    - TODO: Order of growth - see Think Complexity

    Disclaimer: Do not use this function in production. Not all the input and
    output cases were tested.  Use at your own risk.
    """
    def __init__(self, message, letters, method):
        self.message = message
        self.letters = letters
        self.method = method

    def has_message(self):
        cleaned_message = self.clean_message()
        letters_in_bowl = self.clean_letters()

        # print("Message: {}".format(cleaned_message))
        # print("Letters: {}".format(letters_in_bowl))
        print("Message length: {}".format(len(cleaned_message)))
        print("Number of letters: {}".format(len(letters_in_bowl)))

        if self.method == 1:
            method_1 = self.is_message_in_letters_method_1(cleaned_message, letters_in_bowl)
            return method_1
        elif self.method == 2:
            method_2 = self.is_message_in_letters_method_2(cleaned_message, letters_in_bowl)
            return method_2
        elif self.method == 3:
            method_3 = self.is_message_in_letters_method_3(cleaned_message, letters_in_bowl)
            return method_3
        # elif self.method == 4:
        #     method_4 = self.is_message_in_letters_method_4(cleaned_message, letters_in_bowl)
        #     return method_4
        else:
            sys.exit("Method Number {} Is Not Defined.".format(method))

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
        Elements are subtracted from an iterable or from another mapping
        (or counter). Like dict.update() but subtracts counts instead
        of replacing them. Both inputs and outputs may be zero or negative.
        >>> c = Counter(a=4, b=2, c=0, d=-2)
        >>> d = Counter(a=1, b=2, c=3, d=4)
        >>> c.subtract(d)
        >>> c
        Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

        - The two input strings are not the same length (m,s).
        - In the main internal matching cycle, the function immediately interrupts
        processing and returns False, in case there is an element in message with
        no matching in the bowl, avoiding processing the whole message.
        - The worst scenario is when all the message letters are included in the
        alphabet bowl.
        - The method is practically based on the frequency of the items in the bowl.
        - For for Big-O running time there is considered one big cycle to run
        through two possible variables:
            - length of the message (m) and
            - the number of letters in the bowl of soup (s)
        - The solution has a number of iterations, none of them is nested.
        - Time values were taken from the maximum displayed

        The upper frequency amount in created dictionary
        is dictated by the amount of letters in bowl "s".

        Most dictionary operations and methods are constant time

        This solution is O((1))
        - The algorithm does not need optimisation as for big data.

        See "alphabet soup time" tab in attached MS Excel
        """
        print("Method 1")
        message_c = Counter(message)
        letters_c = Counter(letters)
        letters_c.subtract(message_c)
        for letter in message_c.elements():
            if letters_c[letter] < 0:
                return False
        return True

    def is_message_in_letters_method_2(self, message, letters):
        """Algorithm method 2:
        Using similar algorithm as for Anagram Detection Solution 1 at:
        http://interactivepython.org/courselib/static/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html

        "(...)Solution 1: Checking Off
        Our first solution to the anagram problem will check to see that each
        character in the first string actually occurs in the second. If it is
        possible to “checkoff” each character, then the two strings must be
        anagrams. Checking off a character will be accomplished by replacing
        it with the special Python value None. However, since strings in
        Python are immutable, the first step in the process will be to convert
        the second string to a list. Each character from the first string can
        be checked against the characters in the list and if found, checked
        off by replacement.(...)"

        Most list methods are linear

        "(...) each of the n characters in "message - m" will cause an iteration
        through up to "s" characters in the list from "bowl"  (...)"


        "(...) this solution is O((m*s)) (...)"
        - The algorithm does need optimisation as for big data.

        """
        print("Method 2")
        alist = list(letters)

        pos1 = 0
        stillOK = True

        while pos1 < len(message) and stillOK:
            pos2 = 0
            found = False
            while pos2 < len(alist) and not found:
                if message[pos1] == alist[pos2]:
                    found = True
                else:
                    pos2 = pos2 + 1

            if found:
                alist[pos2] = None
            else:
                stillOK = False

            pos1 = pos1 + 1

        return stillOK

    def is_message_in_letters_method_3(self, message, letters):
        """Algorithm method 3:
        Using similar algorithm as for Anagram Detection Solution 2 at:
        http://interactivepython.org/courselib/static/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html

        "(...)Solution 2: Sort and Compare
        Another solution to the anagram problem will make use of the fact that
        even though s1 and s2 are different, they are anagrams only if they
        consist of exactly the same characters. So, if we begin by sorting
        each string alphabetically, from a to z, we will end up with the same
        string if the original two strings are anagrams. ActiveCode 2 shows
        this solution. Again, in Python we can use the built-in sort method
        on lists by simply converting each string to a list at the start.(...)"

        Most list methods are linear
        "(...) Sorting is O(n log n) (...)"

        this solution is O(m log m + s log s)
        - The algorithm does not need optimisation as for big data.

       """
        print("Method 3")
        alist1 = list(message)
        alist2 = list(letters)

        alist1.sort()
        alist2.sort()

        # print("alist1: {}".format(alist1))
        # print("alist2: {}".format(alist2))

        pos1 = 0
        pos2 = 0
        matches = True

        while pos1 < len(message) and matches:
            if alist1[pos1]==alist2[pos2]:
                pos1 = pos1 + 1
                pos2 = pos2 + 1
            else:
                pos2 = pos2 + 1
                if pos2 >= len(alist2):
                    matches = False

        return matches

    def is_message_in_letters_method_4(self, message, letters):
        """

        DO NOT USE!!! Under construction

        TODO: Adapt the algorithm


        Algorithm method 4:
        Using similar algorithm as for Anagram Detection Solution 4 at:
        http://interactivepython.org/courselib/static/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html

        "(...)Solution 4: Count and Compare
        Another solution to the anagram problem will make use of the fact that
        even though s1 and s2 are different, they are anagrams only if they
        consist of exactly the same characters. So, if we begin by sorting
        each string alphabetically, from a to z, we will end up with the same
        string if the original two strings are anagrams. (...) Again, in Python we can use the built-in sort method
        on lists by simply converting each string to a list at the start.(...)"

        "(...) Again, the solution has a number of iterations. However, unlike
        the first solution, none of them are nested. The first two iterations
        used to count the characters are both based on m and s. The third iteration,
        comparing the two lists of counts, always takes 26 steps since there
        are 26 possible characters in the strings. Adding it all up gives us
        T(m*s)=2(m*s)+26 steps. That is O(m*s)

        . We have found a linear order of magnitude algorithm for solving this
        problem.

        Before leaving this example, we need to say something about space
        requirements. Although the last solution was able to run in linear
        time, it could only do so by using additional storage to keep the two
        lists of character counts. In other words, this algorithm sacrificed
        space in order to gain time.

        This is a common occurrence. On many occasions you will need to make
        decisions between time and space trade-offs. In this case, the amount
        of extra space is not significant. However, if the underlying alphabet
        had millions of characters, there would be more concern. As a computer
        scientist, when given a choice of algorithms, it will be up to you to
        determine the best use of computing resources given a particular
        problem. (...)"
        """
        print("Method 4")
        c1 = [0]*94
        c2 = [0]*94

        for i in range(len(message)):
            pos = ord(message[i])-ord('!')
            c1[pos] = c1[pos] + 1

        for i in range(len(letters)):
            pos = ord(letters[i])-ord('!')
            c2[pos] = c2[pos] + 1

        j = 0
        stillOK = True
        while j<94 and stillOK:
            if c1[j]==c2[j]:
                j = j + 1
            else:
                stillOK = False

        return stillOK


if __name__ == '__main__':
    """Main function for module test
    """
    path = ''     # Where input files are located
    method = 1    # Tested method
    test = 1      # <===  Desired iteration test to run
    display_cProfile = 1   # Display cProfile statistics: 1 - Yes

    if test == 1:
        # Test 0001  --> False
        # message = "HelloWorldHH"
        # letters = 'startHeoWordfoospamHh'
        filename_msg = "message_input_0001.txt"
        filename_ltrs = "letters_input_0001.txt"
    elif test == 2:
        # Test 0002 --> True
        # message = "HelloWorldHH"
        # letters = 'startHelloWorldfooHHspamHh'
        filename_msg = "message_input_0002.txt"
        filename_ltrs = "letters_input_0002.txt"
    elif test == 3:
        # Test 0003 --> True -
        # double letters bowl
        # message = "HelloWorldHH"
        # letters = 'startHelloWorldfooHHspamHhstartHelloWorldfooHHspamHh'
        filename_msg = "message_input_0003.txt"
        filename_ltrs = "letters_input_0003.txt"
    elif test == 4:
        # Test 0004 --> True -
        # double in message and bowl
        filename_msg = "message_input_0004.txt"
        filename_ltrs = "letters_input_0004.txt"
    elif test == 5:
        # Test 0005 --> True -
        # in message and "big"  bowl (about 1024)
        filename_msg = "message_input_0005.txt"
        filename_ltrs = "letters_input_0005.txt"
    elif test == 6:
        # Test 0006 --> False -
        # "big"  in message (about 1024),
        # but less letters than in
        # the "big"  bowl 
        filename_msg = "message_input_0006.txt"
        filename_ltrs = "letters_input_0006.txt"
    elif test == 7:
        # Test 0007 --> True -
        # "bigbig"  in message (about 2000)
        # and "2x bigger"  bowl (about 5000)
        filename_msg = "message_input_0007.txt"
        filename_ltrs = "letters_input_0007.txt"
    elif test == 8:
        # Test 0008 --> False -
        # "bigbig"  in message (about 3000)
        # and "same"  bowl 
        filename_msg = "message_input_0008.txt"
        filename_ltrs = "letters_input_0008.txt"
    elif test == 9:
        # Test 0009 --> True
        # REUSED the block to add double block
        # "bigbig"  in message (about 8000)
        # and "bigbig"  bowl (about 19000)
        filename_msg = "message_input_0009.txt"
        filename_ltrs = "letters_input_0009.txt"
    elif test == 10:
        # Test 0010  --> True
        # REUSED the block to add double block
        # "bigbig"  in message (about 15600)
        #  and "bigbig" bowl (about 38000)
        filename_msg = "message_input_0010.txt"
        filename_ltrs = "letters_input_0010.txt"
    else:
        sys.exit("Test Number {} Is Not Defined.".format(test))

    f_msg = codecs.open(path + filename_msg, 'r', 'utf8')
    f_ltrs = codecs.open(path + filename_ltrs, 'r', 'utf8')
    message = f_msg.read()
    letters = f_ltrs.read()
    f_msg.close()
    f_ltrs.close()

    print("Test Nr. : {}".format(test))
    cooking = MainApp(message, letters, method)

    if display_cProfile == 1:
        # Using included profiler
        cProfile.run('cooking.has_message()', 'alphabetsoup.profile')
        p = pstats.Stats('alphabetsoup.profile')
        p.print_stats()

    # Using Elapsed Time calculation (User + System)
    start = etime()
    # put the code you want to measure here
    # Note: first run is sometimes 0   (?!)
    # Needs a second run
    show_me = cooking.has_message()
    end = etime()
    elapsed = end - start

    print("Elapsed Time: {}".format(elapsed))
    print('My message is in the soup: {}'.format(show_me))
