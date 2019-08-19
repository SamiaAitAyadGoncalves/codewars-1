# https://www.codewars.com/kata/57fb04649610ce369a0006b8
#
# # Description:
#
#  Remove some exclamation marks to keep the same number of exclamation marks at
# the beginning and end of each word. Words are separated by spaces in the
# sentence. Please note: only can remove, can not append.
#
# # Examples
#
#
# remove("Hi!") === "Hi"
# remove("!Hi! Hi!") === "!Hi! Hi"
# remove("!!Hi! !Hi!!") === "!Hi! !Hi!"
# remove("!!!!Hi!! !!!!Hi !Hi!!!") === "!!Hi!! Hi !Hi!"
#
#
# # Note
# Please don't post issue about difficulty or duplicate.


def remove(s):
    words = s.split(' ')
    new_words = []

    for word in words:
        count = 0

        for i in range(len(word)//2):
            if word[i] == word[-(i+1)] == '!':
                count += 1
            else:
                break

        new_words.append(count*'!' + word.replace('!', '') + count*'!')

    return ' '.join(new_words)
