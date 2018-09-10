# https://www.codewars.com/kata/5b853229cfde412a470000d0
#
# Your function takes two arguments:
#
#     current father's age (years)
#     current age of his son (years)
#
# Сalculate how many years ago the father was twice as old
# as his son (or in how many years he will be twice as old).


def twice_as_old(dad, son):
    if son / dad == 0.5:
        return 0
    elif son / dad < 0.5:
        s = 1
    elif son / dad > 0.5:
        s = -1
    for i in range(1, dad + 1):
        if (son + s * i) != 0:
            if (dad + s * i) / (son + s * i) == 2:
                return i
