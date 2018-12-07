# https://www.codewars.com/kata/5785cd91a1b8d5c06e000007
#
# There is a sentence which has a mistake in it's ordering.
#
# The part with a capital letter should be the first word.
#
# Please build a function for re-ordering
# Examples
#
# >>> re_ordering('ming Yao')
# 'Yao ming'
#
# >>> re_ordering('Mano donowana')
# 'Mano donowana'
#
# >>> re_ordering('wario LoBan hello')
# 'LoBan wario hello'
#
# >>> re_ordering('bull color pig Patrick')
# 'Patrick bull color pig'


def re_ordering(text):
    arr = text.split(' ')

    for word in arr:
        if word[0].isupper():
            result = word + ' '
            arr.remove(word)

    return result + ' '.join(arr)
