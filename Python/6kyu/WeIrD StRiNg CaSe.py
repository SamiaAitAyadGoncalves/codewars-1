# https://www.codewars.com/kata/52b757663a95b11b3d00062d
#
# Write a function `toWeirdCase` (`weirdcase` in Ruby) that accepts a string, and
# returns the same string with all even indexed characters in each word upper
# cased, and all odd indexed characters in each word lower cased. The indexing just
# explained is zero based, so the zero-ith index is even, therefore that character
# should be upper cased.
#
# The passed in string will only consist of alphabetical characters and spaces(`'
# '`). Spaces will only be present if there are multiple words. Words will be
# separated by a single space(`' '`).
#
# ### Examples:
# javascript
# toWeirdCase( "String" );//=> returns "StRiNg"
# toWeirdCase( "Weird string case" );//=> returns "WeIrD StRiNg CaSe"
#
# coffeescript
# toWeirdCase( "String" );//=> returns "StRiNg"
# toWeirdCase( "Weird string case" );//=> returns "WeIrD StRiNg CaSe"
#
# python
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
#
# haskell
# toWeirdCase "String"            `shouldBe` "StRiNg"
# toWeirdCase "Weird string case" `shouldBe` "WeIrD StRiNg CaSe"
#
# ruby
# weirdcase( "String" )#=> returns "StRiNg"
# weirdcase( "Weird string case" );#=> returns "WeIrD StRiNg CaSe"
#
# php
# toWeirdCase("String"); // => returns "StRiNg"
# toWeirdCase("Weird string case"); // => returns "WeIrD StRiNg CaSe"
#
# go
# toWeirdCase("String") // => returns "StRiNg"
# toWeirdCase("Weird string case") // => returns "WeIrD StRiNg CaSe"


def to_weird_case(string):
    words = string.split(' ')
    new_words = []
    for word in words:
        result = ''
        for i in range(len(word)):
            if i % 2 == 1:
                result += word[i].lower()
            else:
                result += word[i].upper()
        new_words.append(result)
    return ' '.join(new_words)
