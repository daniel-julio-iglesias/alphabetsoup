#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Used for quick and dirty work and testing

count = 10**5
# nums = []
# for i in range(count):
#     nums.append(i)
# nums.reverse()

# nums = []
# for i in range(count):
#     nums.insert(0, i)


# message = 'fkijdff'
message = "Hello, World!"
# letters = 'cvjolalgnfkdbooaslldfgDFGDFglsidjfokasdf'
# letters = 'fkijdff'
letters = 'startHelloWorldfoospamh'


s = "hello, world!"
print("s: {}".format(s))

tokens = s.split()
new_tokens = []
print("Original tokens: {}".format(tokens))
for token in tokens:
    token = token.strip('\'".,?:-!')
    print("token: {}".format(token))
    if token != '':
        new_tokens.append(token)

print("New tokens: {}".format(new_tokens))
new_message = ''.join(new_tokens)
print("New message: {}".format(new_message))

# Learning Python SE
# Page 647 (699 / 1594)

s1 = set('startHelloWorldfoospamh')
s2 = set('HelloWorld')
s2 in s1
False
s1 > s2
True


s1 = set('startelloWorldfoospamh')
s2 = set('HelloWorld')
s1 > s2
False


a = [1,2,3,4,2,3,4,1,2,3]
from collections import Counter
c = Counter(a)
c
c[1]

