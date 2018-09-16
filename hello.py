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


