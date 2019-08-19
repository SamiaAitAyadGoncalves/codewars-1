# https://www.codewars.com/kata/5b180e9fedaa564a7000009a
#
# In this Kata, you will be given a string that may have mixed uppercase and
# lowercase letters and your task is to convert that string to either lowercase only or
# uppercase only based on:
#
# * make as few changes as possible.
# * if the string contains equal number of uppercase and lowercase letters,
# convert the string to lowercase.
#
# For example:
# Haskell
# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to
# lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to
# uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
#
#
# More examples in test cases. Good luck!
#
# Please also try:
#
# [Simple time
# difference](https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2)
#
# [Simple remove
# duplicates](https://www.codewars.com/kata/5ba38ba180824a86850000f7)


def solve(s):
    up = 0
    low = 0

    for letter in s:
        if letter.islower():
            low += 1
        if letter.isupper():
            up += 1
    if up > low:
        return s.upper()
    else:
        return s.lower()
