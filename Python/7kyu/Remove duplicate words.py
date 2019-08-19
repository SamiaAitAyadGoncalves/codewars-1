# https://www.codewars.com/kata/5b39e3772ae7545f650000fc
#
# Your task is to remove all duplicate words from a string, leaving only single
# (first) words entries.
#
# Example:
#
# Input:
#
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma
# delta'
#
# Output:
#
# 'alpha beta gamma delta'


def remove_duplicate_words(s):
    words = s.split(' ')
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    return ' '.join(result)
