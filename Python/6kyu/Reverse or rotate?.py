# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991
#
# The input is a string `str` of digits. Cut the string into chunks (a chunk
# here is a substring of the initial string) of size `sz` (ignore the last
# chunk if its size is less than `sz`).
#
# If a chunk represents an integer such as the **sum of the cubes of its
# digits is divisible by 2**, reverse that chunk; 
# otherwise rotate it to the left by one position.
# Put together these modified chunks and return the result as a string.
#
# If
#
# - `sz` is `<= 0` or if `str` is `empty` return ""
# - `sz` is greater `(>)` than the length of `str` it is impossible to take
# a chunk of size `sz` hence return "".
#
#
# Examples:
# revrot("123456987654", 6) --> "234561876549"
# revrot("123456987653", 6) --> "234561356789"
# revrot("66443875", 4) --> "44668753"
# revrot("66443875", 8) --> "64438756"
# revrot("664438769", 8) --> "67834466"
# revrot("123456779", 8) --> "23456771"
# revrot("", 8) --> ""
# revrot("123456779", 0) --> ""
# revrot("563000655734469485", 4) --> "0365065073456944"


def rot(s):
    return s[1:] + s[0]

def rev(s):
    return s[::-1]

def cube_thingy(s):
    return sum([int(i)**3 for i in s]) % 2 == 0

def revrot(strng, sz):
    result = ''
    l = len(strng)
    if sz <= 0 or strng == '' or sz > l:
        return ''

    blocks = l // sz
    left = l % sz

    for i in range(blocks):
        temp_s = strng[i*sz:i*sz+sz]

        if cube_thingy(temp_s):
            result += rev(temp_s)
        else:
            result += rot(temp_s)

    return result
