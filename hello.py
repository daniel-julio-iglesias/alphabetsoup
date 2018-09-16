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

s = "hello, world!"
print("s: {}".format(s))

tokens = s.split()
new_message = []
print("Original tokens: {}".format(tokens))
for token in tokens:
    token = token.strip('\'".,?:-!')
    print("token: {}".format(token))
    if token != '':
        new_message.append(token)
print("New tokens: {}".format(''.join(new_message)))
