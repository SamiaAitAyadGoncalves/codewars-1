# https://www.codewars.com/kata/52774a314c2333f0a7000688
#
# Write a function called that takes a string of parentheses,
# and determines if the order of the parentheses is valid.
# The function should return true if the string is valid,
# and false if it's invalid.
# Examples
#
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
#
# Constraints
#
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis, input may contain
# any valid ASCII characters. Furthermore, the input string may be
# empty and/or not contain any parentheses at all. Do not treat other
# forms of brackets as parentheses (e.g. [], {}, <>).


def valid_parentheses(string):
    open = []
    close = []
    for i in string:
        if i =="(":
            open.append(1)
            close.append(0)
        elif i ==")":
            open.append(0)
            close.append(1)
        else:
            close.append(0)
            open.append(0)

    result = False
    if sum(open) == sum(close):
        if sum(open) == 0:
            return True

        result = False
        for i in range(len(open)):
            if sum(open[0:i]) >= sum(close[0:i]):
                result = True
            else:
                return False
        return result
    else:
        return result
