# https://www.codewars.com/kata/54da5a58ea159efa38000836
#
# Given an array, find the int that appears an odd number of times.
#
# There will always be only one integer that appears an odd
# number of times.


def find_it(seq):
    s = set(seq)

    for item in s:
        count = 0
        for j in seq:
            if j == item:
                count += 1
        if (count % 2) == 1:
            return item

    return None
