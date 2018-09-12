# https://www.codewars.com/kata/5848565e273af816fb000449
#
# Acknowledgments:
#
# I thank yvonne-liu for the idea and for the example tests :)
# Description:
#
# Encrypt this!
#
# You want to create secret messages which can be deciphered by
# the Decipher this! kata. Here are the conditions:
#
#     Your message is a string containing space separated words.
#     You need to encrypt each word in the message using the
#     following rules:
#         The first letter needs to be converted to its ASCII code.
#         The second letter needs to be switched with the last letter
#     Keepin' it simple: There are no special characters in input.
#
# Examples:
#
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"


def encrypt_this(text):
    if text == '':
        return ''

    t = text.split(' ')
    nw = []
    for i in range(len(t)):
        word = ''
        if len(t[i]) > 2:
            word = str(ord(t[i][0])) + t[i][-1] + t[i][2:-1] + t[i][1]
            nw.append(word)
        else:
            if t[i] != '':
                word = str(ord(t[i][0])) + t[i][1:]
                nw.append(word)

    return ' '.join(nw)
