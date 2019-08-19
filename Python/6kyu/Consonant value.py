# https://www.codewars.com/kata/59c633e7dcc4053512000073
#
# Given a lowercase string that has alphabetic characters only and no spaces,
# return the highest value of consonant substrings. Consonants are any letters of the
# alpahabet except `"aeiou"`.
#
# We shall assign the following values: `a = 1, b = 2, c = 3, .... z = 26`.
#
# For example, for the word "zodiacs", let's cross out the vowels. We get: "z
# **~~o~~** d **~~ia~~** cs"
#
# haskell
# -- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d
# = 4 and cs = 3 + 19 = 22. The highest is 26.
# solve("zodiacs") = 26
#
# For the word "strength", solve("strength") = 57
# -- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 +
# 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.
#
#
# For C: do not mutate input.
#
# More examples in test cases. Good luck!
#
# If you like this Kata, please try:
#
# [Word values](https://www.codewars.com/kata/598d91785d4ce3ec4f000018)
#
# [Vowel-consonant
# lexicon](https://www.codewars.com/kata/59cf8bed1a68b75ffb000026)


import string

def get_dict():
    a = string.ascii_lowercase
    d = {}
    points = 1

    for letter in a:
        d[letter] = points
        points += 1
    return d


def solve(s):
    d = get_dict()
    v = 'aeiou'

    sum_max = 0
    sum = 0
    for letter in s:
        if letter in v:
            if sum >= sum_max:
                sum_max = sum
            sum = 0
        else:
            sum += d[letter]

    return sum_max
