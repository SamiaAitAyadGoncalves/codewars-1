# https://www.codewars.com/kata/5b1e2c04553292dacd00009e
#
# Your task
#
# X and Y are playing a game. A list will be provided which contains
# n pairs of strings and integers. They have to add the integeri to
# the ASCII values of the stringi characters. Then they have to
# check if any of the new added numbers is prime or not. If for any
# character of the word the added number is prime then the word will
# be considered as prime word.
#
# Can you help X and Y to find the prime words?
# Example:
#
# prime_word([["Emma", 30], ["Liam", 30]])  ->  [1, 1]
#
#     For the first word "Emma" ASCII values are: 69 109 109 97
#     After adding 30 the values will be: 99 139 139 127
#     As 139 is prime number so "Emma" is a Prime Word.


import numpy


def prime_word(array):
    a = []
    dim = numpy.shape(array)

    for i in range(dim[0]):
        p_counter = 0
        for j in array[i][0]:
            number = ord(j) + array[i][1]
            print(number)
            if is_prime(number) == True:
                p_counter += 1

        if p_counter > 0:
            a.append(1)
        else:
            a.append(0)

    return a


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
