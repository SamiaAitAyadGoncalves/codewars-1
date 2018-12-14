# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
#
# There is an array with some numbers. All numbers are equal
# except for one. Try to find it!
#
# findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
# findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
#
# It’s guaranteed that array contains more than 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.
#
# This is the first kata in series:
#
#     Find the unique number (this kata)
#     Find the unique string
#     Find The Unique


def find_uniq(arr):
    d = {}

    for number in arr:
        if number not in d:
            d[number] = 1
        else:
            d[number] += 1

    for key, value in d.items():
        if value == 1:
            n = key

    return n
