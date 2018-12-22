# https://www.codewars.com/kata/5a941f4e1a60f6e8a70025fe
#
# You are given an array with several "even" words, one "odd" word, and some
# numbers mixed in.
#
# Determine if any of the numbers in the array is the index of the "odd" word.
# If so, return true, otherwise false.


def odd_ball(arr):
    for i in arr:
        if type(i) == int and i <= len(arr) - 1:
            if arr[i] == 'odd':
                return True
    return False
