# https://www.codewars.com/kata/5441310626bc6a1e61000f2c
#
# Problem
#
# Determine whether a positive integer number is colorful or not.
#
# 263 is a colorful number because [2, 6, 3, 2*6, 6*3, 2*6*3] are all different;
# whereas 236 is not colorful, because [2, 3, 6, 2*3, 3*6, 2*3*6] have 6 twice.
#
# So take all consecutive subsets of digits, take their product and ensure all
# the products are different.
# Examples
#
# 263  -->  true
# 236  -->  false


def colorful(number):
    arr = []
    l=0
    c = str(number)

    while l <= len(c):
        l+=1

        for i in range(len(c)+1 - l):
            prod = 1
            for num in c[i:i+l]:
                prod *= int(num)
            arr.append(prod)

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i] == arr[j]:
                    return False

    return True
