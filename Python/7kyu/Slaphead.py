# https://www.codewars.com/kata/57efab9acba9daa4d1000b30
#
# Being a bald man myself, I know the feeling of needing to keep it clean shaven.
# Nothing worse that a stray hair waving in the wind.
#
# You will be given a string(x). Clean shaved head is shown as "-" and stray
# hairs are shown as "/". Your task is to check the head for stray hairs and get rid of them.
#
# You should return the original string, but with any stray hairs removed.
# Keep count of them though, as there is a second element you need to return:
#
# 0 hairs --> "Clean!"
# 1 hair --> "Unicorn!"
# 2 hairs --> "Homer!"
# 3-5 hairs --> "Careless!"
# >5 hairs --> "Hobo!"
#
# So for this head: "------/------" you should return:
#
# ["-------------", "Unicorn!"]


def bald(s):
    count = 0
    result = ''

    for letter in s:
        if letter == '/':
            count += 1
        result += '-'
    return [result, get_str(count)]


def get_str(count):
    if count == 0:
        return 'Clean!'
    elif count == 1:
        return 'Unicorn!'
    elif count == 2:
        return 'Homer!'
    elif count >= 3 and count <= 5:
        return 'Careless!'
    else:
        return 'Hobo!'
