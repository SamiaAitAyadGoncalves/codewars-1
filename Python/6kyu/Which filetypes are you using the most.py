# https://www.codewars.com/kata/which-filetypes-are-you-using-the-most
#
# Description
# You've been working with a lot of different file types recently
# as your interests have broadend.
#
# But what file types are you using the most? With this question in mind
# we look at the following problem.
#
# Given a List/Array of Filenames (strings) files return a List/Array of
# string(s) contatining the most common extension(s). If there is a tie,
# return all tied extensions sorted first numerically then alphabetically.
#
# Important Info:
#
# Don't forget, you've been working with a lot of different file types,
# so expect some interesting extensions/file names/lengths in the random tests.
#
# Filenames and extensions will contain letters (case sensitive), and numbers.
#
# If a file has multiple extensions (ie: mysong.mp3.als) only count the
# the last extension
#
# Examples:
#
# Example 1:
#
# files = [
#          'Lakey - Better days.mp3',
#          'Wheathan - Superlove.wav',
#          'groovy jam.als',
#          '#4 final mixdown.als',
#          'album cover.ps',
#          'good nights.mp3'
#          ]
#
# Would Return:
# ['.als', .mp3]
#
# As both of the extensions appear two times in files.
#
# Example 2:
#
# files = [
#          'Lakey - Better days.mp3',
#          'Fisher - Stop it.mp3',
#          'Fisher - Losing it.mp3',
#          '#4 final mixdown.als',
#          'album cover.ps',
#          'good nights.mp3'
#          ]
# Would Return:
# ['.mp3']
#
# .MP3 appears more times then any other extension,
# and no other extension has an equal amount of appearences


def solve(files):
    ext = {}

    for file in files:
        temp = '.' + file.split('.')[-1]
        ext.setdefault(temp, 0)
        ext[temp] += 1

    max = 0
    max_items = []

    for key, val in ext.items():

        if val > max:
            max = val
            del max_items
            max_items = [key]

        if val == max and key not in max_items:
            max_items.append(key)

    max_items.sort()
    return max_items
