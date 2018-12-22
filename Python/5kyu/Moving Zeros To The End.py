# https://www.codewars.com/kata/52597aa56021e91c93000cb0
#
# Write an algorithm that takes an array and moves all of the zeros to the
# end, preserving the order of the other elements.
#
# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]


def move_zeros(array):
    count = 0
    result = []

    for item in array:
        if item == 0 and (type(item) == int or type(item) == float):
            count += 1
        else:
            result.append(item)

    for i in range(count):
        result.append(0)

    return result
