# https://www.codewars.com/kata/573992c724fc289553000e95
#
# You have a positive number n consisting of digits. You can do at most one
# operation: Choosing the index of a digit in the number, remove this digit
# at that index and insert it back to another place in the number.
#
# Doing so, find the smallest number you can get.
#
# #Task: Return an array or a tuple or a string depending on the language
# #(see "Sample Tests") with
#
#     1) the smallest number you got
#     2) the index i of the digit d you took, i as small as possible
#     3) the index j (as small as possible) where you insert this digit
#        d to have the smallest number.
#
# Example:
#
# smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"
#
# 126235 is the smallest number gotten by taking 1 at index 2 and
# putting it at index 0
#
# smallest(209917) --> [29917, 0, 1] or ...
#
# [29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0]
# is greater than
# index `i` in [29917, 0, 1].
#
# 29917 is the smallest number gotten by taking 2 at index 0 and putting
# it at index 1 which gave 029917 which is the number 29917.
#
# smallest(1000000) --> [1, 0, 6] or ...
#
# Note
#
# Have a look at "Sample Tests" to see the input and output in each language

def move(s, i, j):
    result = ''
    for k in range(len(s)):
        if k != i:
            result += s[k]
    return result[:j] + s[i] + result [j:]


def smallest(n):
    s = str(n)
    numbers = [[s, 0, 0]]

    for i in range(len(numbers[0][0])):
        for j in range(len(numbers[0][0])):
            numbers.append([move(s, i, j), i, j])

    mini = numbers[0]
    for element in numbers:
        if element[0] <= mini[0]:
            mini = element

    for element in numbers:
        if element[0] == mini[0] and element[1] <= mini[1]:
            mini = element

    for element in numbers:
        if element[0] == mini[0] and element[1] == mini[1] and element[2] <= mini[2]:
            mini = element

    mini[0] = int(mini[0])

    return mini
