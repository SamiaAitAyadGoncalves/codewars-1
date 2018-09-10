# https://www.codewars.com/kata/57eae65a4321032ce000002d
#
# Given a string of digits, you should replace any digit
# below 5 with '0' and any digit 5 and above with '1'.
# Return the resulting string.


def fake_bin(x):
    fake_binary = ''
    for char in x:
        if int(char) < 5:
            fake_binary = fake_binary + '0'
        else:
            fake_binary = fake_binary + '1'
    return fake_binary
