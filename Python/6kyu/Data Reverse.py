# https://www.codewars.com/kata/569d488d61b812a0f7000015
#
# A stream of data is received and needs to be reversed. Each segment
# is 8 bits long, meaning the order of these segments need to be
# reversed, for example:
#
# 11111111  00000000  00001111  10101010
#   byte1     byte2     byte3     byte4
#
# should become:
#
# 10101010  00001111  00000000  11111111
#   byte4     byte3     byte2     byte1
#
# The total number of bits will always be a multiple of 8. The data is
# given in an array as such:
#
# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]


def data_reverse(data):
    old = ''.join([str(i) for i in data])
    new = ''
    l = len(old)

    while True:
        new = new + old[-8:]
        old = old[:-8]

        if len(new) == l:
            return [int(i) for i in new]
