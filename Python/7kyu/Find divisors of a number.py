# https://www.codewars.com/kata/542c0f198e077084c0000c2e
#
# Find the number of divisors of a positive integer n.
#
# Random tests go up to n = 500000.
# Examples
#
# divisors(4)  = 3  # 1, 2, 4
# divisors(5)  = 2  # 1, 5
# divisors(12) = 6  # 1, 2, 3, 4, 6, 12
# divisors(30) = 8  # 1, 2, 3, 5, 6, 10, 15, 30


def divisors(n):
    count = 1 # 1 is always divisor of n
    for i in range(1,n): # if n=1 this loops over an empty set
        if n % i == 0:
            count += 1
    return count
