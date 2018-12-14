# https://www.codewars.com/kata/5b55c49d4a317adff500015f
#
# You have the radius of a circle with the center in point (0,0).
#
# Write a function that calculates the number of points in the circle
# where (x,y) - the cartesian coordinates of the points - are integers.
#
# Example: for radius = 2 the result should be 13.
#
# 0 <= radius <= 1000


def points(n):
    sum = 1
    n2 = n**2
    k = [i*i for i in range(n+1)]

    for i in k:
        if i != 0:
            for j in k:
                if i + j <= n2:
                    sum += 4
    return sum
