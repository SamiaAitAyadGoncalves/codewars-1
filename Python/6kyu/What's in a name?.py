# https://www.codewars.com/kata/59daf400beec9780a9000045
#
# <h1>What's in a name?</h1>
# ..Or rather, what's a name in? For us, a particular string is where we are
# looking for a name.
#
# <h2>Task</h2>
#
# Test whether or not the string contains all of the letters which spell a given
# name, in order.
#
# <h2>The format</h2>
# A function passing two strings, searching for one (the name) within the other.
# ``function nameInStr(str, name){ return true || false }``
#
# <h2>Examples</h2>
#
#     nameInStr('Across the rivers', 'chris') --> true
#                 ^      ^  ^^   ^
#                 c      h  ri   s
#
#     Contains all of the letters in 'chris', in order.
# ----------------------------------------------------------
#     nameInStr('Next to a lake', 'chris') --> false
#
#     Contains none of the letters in 'chris'.
# --------------------------------------------------------------------
#     nameInStr('Under a sea', 'chris') --> false
#                    ^   ^
#                    r   s
#
#     Contains only some of the letters in 'chris'.
# --------------------------------------------------------------------
#     nameInStr('A crew that boards the ship', 'chris') --> false
#                  cr    h              s i
#                  cr                h  s i
#                  c     h      r       s i
#                  ...
#
#     Contains all of the letters in 'chris', but not in order.
# --------------------------------------------------------------------
#     nameInStr('A live son', 'Allison') --> false
#                ^ ^^   ^^^
#                A li   son
#
#     Contains all of the correct letters in 'Allison', in order,
#     but not enough of all of them (missing an 'l').
#
#
# Note: testing will _not_ be case-sensative.


def name_in_str(s, name):
    n = list(name.lower())
    for letter in s.lower():
        if letter == n[0]:
            n.pop(0)
        if n == []:
            return True
    return False
