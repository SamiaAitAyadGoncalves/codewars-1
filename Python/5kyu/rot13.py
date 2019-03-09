# https://www.codewars.com/kata/530e15517bc88ac656000716
#
# ROT13 is a simple letter substitution cipher that replaces a letter with
# the letter 13 letters after it in the alphabet. ROT13 is an example of
# the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with
# Rot13. If there are numbers or special characters included in the string,
# they should be returned as they are. Only letters from the latin/english
# alphabet should be shifted, like in the original Rot13 "implementation".
#
# Please note that using encode is considered cheating.


import string

def rot13(message):
    a1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a2 = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'

    result = ''
    for letter in message:
        if letter in a1:
            k = a1.find(letter)
            result = result + a2[k]
        else:
            result = result + letter

    return result
