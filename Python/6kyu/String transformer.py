# https://www.codewars.com/kata/5878520d52628a092f0002d0
#
# Given a string, return a new string that has transformed based on the input:
#
# * Change case of every character, ie. lower case to upper case, upper case to
# lower case.
# * Reverse the order of words from the input.
#
# **Note:** You will have to handle multiple spaces, and leading/trailing spaces.
#
# For example:
#
#
# "Example Input" ==> "iNPUT eXAMPLE"
#
#
# You may assume the input only contain English alphabet and spaces.


def string_transformer(s):
    words = s.split(' ')
    new_words = []

    for word in words:
        new_word = ''
        for letter in word:
            if letter.isupper():
                new_word += letter.lower()
            elif letter.islower():
                new_word += letter.upper()
            else:
                new_word += letter
        new_words.append(new_word)

    return ' '.join(new_words[::-1])
