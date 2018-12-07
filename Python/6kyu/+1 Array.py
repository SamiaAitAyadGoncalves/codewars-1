# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9
#
# Given an array of integers of any length, return an array that has 1
# added to the value represented by the array.
#
# For example an array [2, 3, 9] equals 239, add one would return
# an array [2, 4, 0].
#
# [4, 3, 2, 5] would return [4, 3, 2, 6]
#
#     the array can't be empty
#     only non-negative, single digit integers are allowed
#
# Return nil (language equivalent) for invalid inputs


def up_array(arr):
    if arr == []:
        return None

    s = ''
    for item in arr:
        if item < 0 or item > 9:
            return None
        s += str(item)

    number = int(s) + 1

    return [int(i) for i in str(number)]
