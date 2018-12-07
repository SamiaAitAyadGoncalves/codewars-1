# https://www.codewars.com/kata/56a4872cbb65f3a610000026
#
# Take a number: 56789. Rotate left, you get 67895.
#
# Keep the first digit in place and rotate left the other digits: 68957.
#
# Keep the first two digits in place and rotate the other ones: 68579.
#
# Keep the first three digits and rotate left the rest: 68597. Now it is
# over since keeping the first four it remains only one digit which rotated is
# itself.
#
# You have the following sequence of numbers:
#
# 56789 -> 67895 -> 68957 -> 68579 -> 68597
#
# and you must return the greatest: 68957.
#
# Calling this function max_rot (or maxRot or ... depending on the language)
#
# max_rot(56789) should return 68957


def rot(n):
    return n[1:]+n[0]

def max_rot(n):
    numbers = [str(n)]

    for i in range(len(numbers[0])-1):
        numbers.append(numbers[-1][:i]+rot(numbers[-1][i:]))

    return max([int(n) for n in numbers])
