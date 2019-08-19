# https://www.codewars.com/kata/54e6533c92449cc251001667
#
# Implement the function unique_in_order which takes as argument a sequence and
# returns a list of items without any elements with the same value next to each
# other and preserving the original order of elements.
#
# For example:
#
# javascript
# uniqueInOrder('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# uniqueInOrder('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# uniqueInOrder([1,2,2,3,3])       == [1,2,3]
#
# python
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
#
# ruby
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
#
# haskell
# uniqueInOrder "AAAABBBCCDAABBB" == "ABCDAB"
# uniqueInOrder "ABBCcAD"         == "ABCcAD"
# uniqueInOrder [1,2,2,3,3]       == [1,2,3]
#
# crystal
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
#
# rust
# unique_in_order("AAAABBBCCDAABBB".chars()) == vec!['A', 'B', 'C', 'D', 'A',
# 'B']
# unique_in_order("ABBCcAD")                 == vec!['A', 'B', 'C', 'c', 'A',
# 'D']
# unique_in_order(vec![1,2,2,3,3])           == vec![1,2,3]


def unique_in_order(iterable):
    if iterable == '' or iterable == []:
        return []

    result = [iterable[0]]
    for item in iterable:
        if item != result[-1]:
            result.append(item)

    return result
