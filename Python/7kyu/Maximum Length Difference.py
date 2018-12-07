# https://www.codewars.com/kata/5663f5305102699bad000056
#
# You are given two arrays a1 and a2 of strings. Each string is composed
# with letters from a to z. Let x be any string in the first array and y
# be any string in the second array.
#
# Find max(abs(length(x) − length(y)))
#
# If a1 and/or a2 are empty return -1 in each language except in Haskell
# (F#) where you will return Nothing (None).
#
# #Example:
#
# a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa",
# "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# mxdiflg(a1, a2) --> 13
#
# Bash note:
#
#     input : 2 strings with substrings separated by ,
#     output: number as a string


def find_max(arr):
    max = len(arr[0])
    for word in arr:
        if len(word) > max:
            max = len(word)
    return max

def find_min(arr):
    min = len(arr[0])
    for word in arr:
        if len(word) < min:
            min = len(word)
    return min

def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    else:
        return max(abs(find_max(a1)-find_min(a2)),abs(find_max(a2)-find_min(a1)))
