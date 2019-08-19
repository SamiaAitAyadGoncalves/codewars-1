# https://www.codewars.com/kata/5a91e0793e9156ccb0003f6e
#
# Given a name, turn that name into a perfect square matrix (nested array with the
# amount of arrays equivalent to the length of each array).
#
# You will need to add periods (`.`) to the end of the name if necessary, to turn
# it into a matrix.
#
# If the name has a length of 0, return `"name must be at least one letter"`
#
# ## Examples
#
# js
# "Bill" ==> [ ["B", "i"],
#              ["l", "l"] ]
#
# "Frank" ==> [ ["F", "r", "a"],
#               ["n", "k", "."],
#               [".", ".", "."] ]


def matrixfy(st):
    if st == '':
        return "name must be at least one letter"

    l = len(st)
    i = 0
    while i*i < l:
        i += 1
    s = st.ljust(i*i, '.')

    result = []
    temp = []
    c = 0
    for j in range(i*i):
        temp.append(s[j])
        c += 1
        if c == i:
            c = 0
            result.append(temp)
            temp= []

    return result
