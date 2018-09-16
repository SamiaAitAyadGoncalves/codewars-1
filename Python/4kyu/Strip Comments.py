# https://www.codewars.com/kata/strip-comments/python
#
# Complete the solution so that it strips all text that
# follows any of a set of comment markers passed in.
# Any whitespace at the end of the line should also be stripped out.
#
# Example:
#
# Given an input string of:
#
# apples, pears # and bananas
# grapes
# bananas !apples
#
# The output expected would be:
#
# apples, pears
# grapes
# bananas
#
# The code would be called like so:
#
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples",
#  ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"


def solution(string,markers):
    s = list(string)
    result = []
    indicator = 0

    for i in range(len(s)):
        if s[i] in markers:
            indicator = 1

            temp = ''.join(result)
            if temp != '':
                while temp[-1] == ' ':
                    temp = temp[:-1]
            result = list(temp)

        elif '\n' == s[i]:
            result.append(s[i])
            indicator = 0

        else:
            if indicator == 0:
                result.append(s[i])

    if result == []:
        return ''
    else:
        r = ''.join(result)
        while r[-1] == ' ':
            r = r[:-1]
        return r
