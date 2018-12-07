# https://www.codewars.com/kata/554e52e7232cdd05650000a0
#
# Create a function that returns the lowest product of 4 consecutive digits
# in a number given as a string.
#
# This should only work if the number has 4 digits or more. If not,
# return "Number is too small".
#
# ##Example
#
# lowest_product("123456789")--> 24 (1x2x3x4)
# lowest_product("35") --> "Number is too small"


def product(n):
    l = [int(i) for i in n]
    result = 1
    for i in l:
        result *= i
    return result


def lowest_product(input):
    if len(input) < 4:
        return "Number is too small"
    else:
        numbers = []
        for i in range(len(input)-3):
            numbers.append(product(input[i:i+4]))
        return min(numbers)
