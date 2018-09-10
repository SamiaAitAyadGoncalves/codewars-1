# https://www.codewars.com/kata/5a9e86705ee396d6be000091
#
# Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran), check if the array contains three and two of the same values.
# Examples
#
# ["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
# ["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
# ["a", "a", "a", "a", "a"] ==> false // 5x "a"


def check_three_and_two(array):
    a_count, b_count, c_count = 0, 0, 0
    for i in range(5):
        if array[i] == 'a':
            a_count += 1
        if array[i] == 'b':
            b_count += 1
        if array[i] == 'c':
            c_count += 1

    if 0 in [a_count, b_count, c_count]:
        if 2 in [a_count, b_count, c_count]:
            if 3 in [a_count, b_count, c_count]:
                return True
    return False
