# https://www.codewars.com/kata/5970df092ef474680a0000c9
#
# The alphabetized kata
# ---------------------
#
# Re-order the characters of a string, so that they are concatenated into a
# new string in "case-insensitively-alphabetical-order-of-appearance" order.
# Whitespace and punctuation shall simply be removed!
#
# The input is restricted to contain no numerals and only words
# containing the english alphabet letters.
#
# Example:
#
# javascript
# alphabetized("The Holy Bible") // "BbeehHilloTy"
#
# cpp
# alphabetized("The Holy Bible") // "BbeehHilloTy"
#
# python
# alphabetized("The Holy Bible") # "BbeehHilloTy"
#
# ruby
# alphabetized("The Holy Bible") # "BbeehHilloTy"
#
# crystal
# alphabetized("The Holy Bible") # "BbeehHilloTy"
#
# haskell
# alphabetized "The Holy Bible" -- "BbeehHilloTy"
#
# c
# alphabetized ("The Holy Bible") // "BbeehHilloTy"
#
#
#
# _Inspired by [Tauba Auerbach](http://www.taubaauerbach.com/view.php?id=73)_


def alphabetized(s):
    l = list(s.replace(' ', ''))
    l.sort(key=str.lower)
    return ''.join([i for i in l if i.isalpha()])
