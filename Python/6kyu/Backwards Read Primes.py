# https://www.codewars.com/kata/5539fecef69c483c5a000015
#
# Description:
#
# Backwards Read Primes are primes that when read backwards in base 10
# (from right to left) are a different prime. (This rules out primes
# which are palindromes.)
#
# Examples:
# 13 17 31 37 71 73 are Backwards Read Primes
#
# 13 is such because it's prime and read from right to left writes 31
# which is prime too. Same for the others.
# Task
#
# Find all Backwards Read Primes between two positive given numbers
# (both inclusive), the second one always being greater than or equal to
# the first one. The resulting array or the resulting string will be ordered
# following the natural order of the prime numbers.
# Example
#
# backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97]
# backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]
# backwardsPrime(501, 599) => []
#
# backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97]
# backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]


def is_prime(n):
    import math
    a = math.ceil(math.sqrt(n))+1
    for i in range(7,a,2):
        if n % i == 0:
            return False
    return True

def backwardsPrime(start, stop):
    result = []
    cand = [i for i in range(start, stop+1) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]

    for number in cand:
        a = int(str(number)[::-1])
        if a % 2 != 0 and a % 5 != 0 and a != number:
            if is_prime(number):
                if is_prime(a):
                    result.append(number)

    return result
