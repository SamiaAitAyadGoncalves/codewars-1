# https://www.codewars.com/kata/513e08acc600c94f01000001
#
# The rgb() method is incomplete. Complete the method so that passing in
# RGB decimal values will result in a hexadecimal representation being returned.
# The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that
# fall out of that range should be rounded to the closest valid value.
#
# The following are examples of expected output values:
#
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


def rgb(r, g, b):
    d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', \
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    result = ''
    c = [r, g, b]
    for i in range(3):
        if c[i] >= 255:
            c[i] = 255
        if c[i] <= 0:
            c[i] = 0

    for col in c:
        result += d[col // 16]+d[col % 16]

    return result
