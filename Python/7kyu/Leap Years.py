# https://www.codewars.com/kata/526c7363236867513f0005ca
#
# In this kata you should simply determine, whether a given year is a leap year
# or not. In case you don't know the rules, here they are:
#
#     years divisible by 4 are leap years
#     but years divisible by 100 are no leap years
#     but years divisible by 400 are leap years
#
# Additional Notes:
#
#     Only valid years (positive integers) will be tested, so you don't have
#     to validate them
#
# Examples can be found in the test fixture.


def isLeapYear(year):
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True
    return leap
