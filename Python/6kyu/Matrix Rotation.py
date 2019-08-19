# https://www.codewars.com/kata/593e978a3bb47a8308000b8f
#
# Given a matrix represented as a list of string, such as
#
# ###.....
# ..###...
# ....###.
# .....###
# .....###
# ....###.
# ..###...
# ###.....
#
# write a function
# if:javascript
# `rotateClockwise(matrix)`
#
# if:ruby,python
# `rotate_clockwise(matrix)`
#
# that return its 90° clockwise rotation, for our example:
#
#
# #......#
# #......#
# ##....##
# .#....#.
# .##..##.
# ..####..
# ..####..
# ...##...
#
# > <strong style="color:red;"> /!\ </strong> You must return a **rotated copy**
# of `matrix`! (`matrix` must be the same before and after calling your function)
#
# > Note that the matrix isn't necessarily a square, though it's always a
# rectangle!
# > Please also note that the equality `m ==
# rotateClockwise(rotateClockwise(rotateClockwise(rotateClockwise(m))));` (360° clockwise rotation), is not always true
# because `rotateClockwise([''])` => `[]` and `rotateClockwise(['','',''])` =>
# `[]` (empty lines information is lost)


def rotate_clockwise(matrix):
    if matrix == []: return []

    temp = []

    for line in matrix:
        temp.append(list(line))

    r = []
    for i in range(len(temp[0])):
        temp = ''
        for line in matrix[::-1]:
            temp += line[i]
        r.append(temp)

    return r
