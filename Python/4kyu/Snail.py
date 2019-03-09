# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
#
# Snail Sort
#
# Given an n x n array, return the array elements arranged from outermost
# elements to the middle element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
#
# For better understanding, please follow the numbers of the next array
# consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
#
# NOTE: The idea is not sort the elements from the lowest value to the highest;
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as [[]]


import math

def snail(array):
    n = len(array)
    result = []

    if array == [[]]:
        return result

    for i in range(int(n/2)):
        for j in range(n-i*2):
            result.append(array[i][j+i])

        for j in range(n-i*2-1):
            result.append(array[1+i+j][n-i-1])

        for j in range(n-i*2-1):
            result.append(array[n-i-1][n-i-2-j])

        for j in range(n-i*2-2):
            result.append(array[n-i-2-j][0+i])

    if n % 2 != 0:
        result.append(array[math.floor(n/2)][math.floor(n/2)])

    return result
