# https://www.codewars.com/kata/positions-average/python
#
# Suppose you have 4 numbers: '0', '9', '6', '4' and 3 strings
# composed with them:
#
# s1 = "6900690040"
# s2 = "4690606946"
# s3 = "9990494604"
#
# Compare s1 and s2 to see how many positions they have in common:
# 0 at index 3, 6 at index 4, 4 at index 8 ie 3 common positions
# out of ten.
#
# Compare s1 and s3 to see how many positions they have in common:
# 9 at index 1, 0 at index 3, 9 at index 5 ie 3 common positions
# out of ten.
#
# Compare s2 and s3. We find 2 common positions out of ten.
#
# So for the 3 strings we have 8 common positions out of 30 ie 0.2666...
# or 26.666...%
#
# Given a set of n strings our function pos_average will calculate
# the average percentage of positions that are the same between
# the (n * (n-1)) / 2 sets of strings taken amongst the given 'n' strings.
#
# The function returns the percentage formatted as a float
# with 10 decimals but the result is tested at 1e.-9
# (see function assertFuzzy in the tests).
#
# Example:
#
# Given string s = "444996, 699990, 666690, 096904, 600644,
# 640646, 606469, 409694, 666094, 606490" composing a set of
# n = 10 substrings (hence 45 combinations), pos_average
# returns 29.2592592593.
#
# In a set the n strings will have the same length ( > 0 ).
# Notes
#
#     You can see other examples in the "Sample tests".
#     Translators are welcome for all languages, except
#     for Ruby since the Bash random tests needing Ruby
#     a Ruby reference solution is already there though
#     not yet published.


def av_per(n):
    return (n * (n-1)) / 2

def pos_average(s):
    new_s = s.split(', ')
    count = 0

    for i in range(len(new_s)):
        for j in range(len(new_s)):
            if i < j:
                for k in range(len(new_s[i])):
                    if new_s[i][k] == new_s[j][k]:
                        count += 1

    result = 100*count / (av_per(len(new_s))*len(new_s[i]))

    return result
