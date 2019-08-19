# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
#
# Write function isPalindrome that checks if a given string (case insensitive) is
# a palindrome.


def is_palindrome(s):
    return s.lower() == s[::-1].lower()
