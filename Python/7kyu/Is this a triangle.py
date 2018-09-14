# https://www.codewars.com/kata/is-this-a-triangle/python
#
# Implement a method that accepts 3 integer values a, b, c.
# The method should return true if a triangle can be built
# with the sides of given length and false in any other case.
#
# (In this case, all triangles must have surface greater
# than 0 to be accepted).


def is_triangle(a, b, c):

    if(a<=abs(b-c)) or (b<=abs(a-c)) or (c<=abs(a-b)):
        return False
    else:
        return True
