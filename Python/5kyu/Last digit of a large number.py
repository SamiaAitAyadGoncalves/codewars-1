# https://www.codewars.com/kata/5511b2f550906349a70004e1
#
# Define a function that takes in two non-negative integers a and b and
# returns the last decimal digit of a^b. Note that a and b may be very large!
#
# For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969.
# The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal
# digits, is 6. Also, please take 0^0 to be 1.
#
# You may assume that the input will always be valid.
# Examples
#
# last_digit(4, 1)                # returns 4
# last_digit(4, 2)                # returns 6
# last_digit(9, 7)                # returns 9
# last_digit(10, 10 ** 10)        # returns 0
# last_digit(2 ** 200, 2 ** 300)  # returns 6


def last_digit(n1, n2):
    if n2 == 0:
        return 1

    n1 = int(str(n1)[-1])

    if n1 in (0,1,5,6):
        return n1

    elif n1 in (4,9):
        if n2 % 2 == 0:
            return int(str(n1**2)[-1])
        else:
            return n1

    elif n1 in (2,3,7,8):
        if n2 % 4 == 0:
            return int(str(n1**4)[-1])
        if n2 % 4 == 3:
            return int(str(n1**3)[-1])
        if n2 % 4 == 2:
            return int(str(n1**2)[-1])
        else:
            return n1
