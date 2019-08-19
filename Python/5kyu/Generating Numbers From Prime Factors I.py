# https://www.codewars.com/kata/58f9f9f58b33d1b9cf00019d
#
# Given a list of prime factors, primesL, and an integer, limit, try to
# generate in order, all the numbers less than the value of limit, that
# have **all and only** the prime factors of primesL
#
# ## Example
# py
# primesL = [2, 5, 7]
# limit = 500
# List of Numbers Under 500          Prime Factorization
# ___________________________________________________________
#            70                         [2, 5, 7]
#           140                         [2, 2, 5, 7]
#           280                         [2, 2, 2, 5, 7]
#           350                         [2, 5, 5, 7]
#           490                         [2, 5, 7, 7]
#
#
# There are 5 of these numbers under 500 and the largest one is 490.
#
# ## Task
#
# For this kata you have to create the function count_find_num(),
# that accepts two arguments: primesL and limit, and returns the
# amount of numbers that fulfill the requirements, and the largest
# number under `limit`.
#
# The example given above will be:
# python
# primesL = [2, 5, 7]
# limit = 500
# count_find_num(primesL, val) == [5, 490]
#
#
# If no numbers can be generated under `limit` then return an empty list:
# python
# primesL = [2, 3, 47]
# limit = 200
# find_nums(primesL, limit) == []
#
#
# The result should consider the limit as inclusive:
# python
# primesL = [2, 3, 47]
# limit = 282
# find_nums(primesL, limit) == [1, 282]
#
#
# Features of the random tests:
#
# number of tests = 200
# 2 <= length_primesL <= 6 // length of the given prime factors array
# 5000 <= limit <= 1e17
# 2 <= prime <= 499  // for every prime in primesL
#
#
# Enjoy!


def get_numbers(numbers, ls, prod, limit):
    for item in set(ls):
        new_prod = prod*item
        if new_prod <= limit:
            numbers.append(new_prod)
            ls.append(item)
            get_numbers(numbers, ls, new_prod, limit)


def count_find_num(primesL, limit):
    prod = 1

    for item in primesL:
        prod *= item
    if prod > limit:
        return []

    numbers = [prod]
    get_numbers(numbers, primesL, prod, limit)
    sort_num = sorted(set(numbers))

    return [len(sort_num), sort_num[-1]]
