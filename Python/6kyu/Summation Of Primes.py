# https://www.codewars.com/kata/59ab0ca4243eae9fec000088
#
# Summation Of Primes
#
# The sum of the primes below or equal to 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below or equal to the number passed in.
#
# From Project Euler's Problem #10.


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def summationOfPrimes(primes):
    return sum([i for i in range(primes+1) if is_prime(i) == True])-1
