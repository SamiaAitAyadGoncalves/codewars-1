# https://www.codewars.com/kata/5894318275f2c75695000146
#
# Task
#
# Given an integer n, find the maximal number you can obtain by deleting
# exactly one digit of the given number.
# Example
#
# For n = 152, the output should be 52;
#
# For n = 1001, the output should be 101.
# Input/Output
#
#     [input] integer n
#
#     Constraints: 10 ≤ n ≤ 1000000.
#
#     [output] an integer


def delete_digit(n):
    s = str(n)
    arr = []

    for i in range(len(s)):
        new_s = ''
        for j in range(len(s)):
            if i != j:
                new_s += s[j]
        arr.append(int(new_s))
    return max(arr)
