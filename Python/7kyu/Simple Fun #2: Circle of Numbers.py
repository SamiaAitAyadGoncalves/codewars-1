# https://www.codewars.com/kata/58841cb52a077503c4000015
#
# Task
#
# Consider integer numbers from 0 to n - 1 written down along the circle in
# such a way that the distance between any two neighbouring numbers is equal
# (note that 0 and n - 1 are neighbouring, too).
#
# Given n and firstNumber/first_number, find the number which is written in
# the radially opposite position to firstNumber.
# Example
#
# For n = 10 and firstNumber = 2, the output should be
#
# circleOfNumbers(n, firstNumber) === 7
#
# Input/Output
#
#     [input] integer n
#
#     A positive even integer.
#
#     Constraints: 4 ≤ n ≤ 1000.
#
#     [input] integer firstNumber/first_number
#
#     Constraints: 0 ≤ firstNumber ≤ n - 1
#
#     [output] an integer


def circle_of_numbers(n, fst):
    return [i for i in range(n)][int((fst + n/2) % n)]
