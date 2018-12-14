# https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f
#
# Find the sum of the digits of all the numbers from 1 to N (both ends included).
# Examples
#
# # N = 4
# 1 + 2 + 3 + 4 = 10
#
# # N = 10
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46
#
# # N = 12
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51


def compute_sum(n):
    sum = 0
    for i in range(n+1):
        if len(str(i)) == 1:
            sum += i
        else:
            m = str(i)
            for j in m:
                sum += int(j)
    return sum
