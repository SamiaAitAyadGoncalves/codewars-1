# https://www.codewars.com/kata/5a8059b1fd577709860000f6
#
# Your task is very simple. Just write a function `isAlphabetic(s)`, which takes
# an input string `s` in lowercase and returns `true`/`false` depending on whether
# the string is in alphabetical order or not.
#
# For example, `isAlphabetic('kata')` is False as 'a' comes after 'k', but
# `isAlphabetic('ant')` is True.
#
# Good luck :)


def alphabetic(s):
    return s==''.join(sorted(s))
