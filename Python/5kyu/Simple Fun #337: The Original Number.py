# https://www.codewars.com/kata/5959b637030042889500001d
#
# Task
#
# John has an important number, and he doesn't want others to see it.
#
# He decided to encrypt the number, using the following steps:
#
# His number is always a non strict increasing sequence
# ie. "123"
#
# He converted each digit into English words.
# ie. "123"--> "ONETWOTHREE"
#
# And then, rearrange the letters randomly.
# ie. "ONETWOTHREE" --> "TTONWOHREEE"
#
# John felt that his number were safe in doing so. In fact, such encryption
# can be easily decrypted :(
#
# Given the encrypted string s, your task is to decrypt it, return the original
# number in string format.
#
# Note, You can assume that the input string s is always valid; It contains
# only uppercase Letters; The decrypted numbers are arranged in ascending
# order; The leading zeros are allowed.
# Example
#
# For s = "ONE", the output should be 1.
#
# For s = "EON", the output should be 1 too.
#
# For s = "ONETWO", the output should be 12.
#
# For s = "OONETW", the output should be 12 too.
#
# For s = "ONETWOTHREE", the output should be 123.
#
# For s = "TTONWOHREEE", the output should be 123 too.


def original_number(s):
    s = sorted(s)
    d = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', \
    4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}

    sp = {0: 'Z', 1: 'O', 2: 'W', 3: 'H', 4: 'R', 5: 'V', 6: 'X', 7: 'S', 8: 'G', 9: 'I'}

    l = [0, 2, 6, 8, 3, 4, 7, 5, 1, 9]
    c = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}


    for number in l:
        while sp[number] in s:
            for letter in d[number]:
                s.remove(letter)
            c[number] += 1

    result = []
    for i in range(10):
        result += [str(i)]*c[i]

    return ''.join(result)
