# https://www.codewars.com/kata/5656b6906de340bd1b0000ac
#
# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted
# string, the longest possible, containing distinct letters,
#
#     each taken only once - coming from s1 or s2. #Examples:
#     ``` a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b)
#     -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz" longest(a, a)
# -> "abcdefghijklmnopqrstuvwxyz" ```


def longest(s1, s2):
    import string
    a = string.ascii_lowercase
    result = ''
    s = s1 + s2
    for letter in a:
        if letter in s and letter not in result:
            result += letter
    return result
