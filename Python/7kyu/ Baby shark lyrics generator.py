# https://www.codewars.com/kata/5d076515e102162ac0dc514e
#
# # Baby Shark Lyrics
#
# ![baby shark](https://www.gannett-cdn.com/presto/2019/06/05/USAT/95adf0c6-9d32-4fcc-8b60-5b6bd3e04310-Baby_Shark_image.jpg?width=1080&quality=50)
#
# Create a function, as short as possible, that returns this lyrics.
# Your code should be less than `300` characters.
#
#
# Baby shark, doo doo doo doo doo doo
# Baby shark, doo doo doo doo doo doo
# Baby shark, doo doo doo doo doo doo
# Baby shark!
# Mommy shark, doo doo doo doo doo doo
# Mommy shark, doo doo doo doo doo doo
# Mommy shark, doo doo doo doo doo doo
# Mommy shark!
# Daddy shark, doo doo doo doo doo doo
# Daddy shark, doo doo doo doo doo doo
# Daddy shark, doo doo doo doo doo doo
# Daddy shark!
# Grandma shark, doo doo doo doo doo doo
# Grandma shark, doo doo doo doo doo doo
# Grandma shark, doo doo doo doo doo doo
# Grandma shark!
# Grandpa shark, doo doo doo doo doo doo
# Grandpa shark, doo doo doo doo doo doo
# Grandpa shark, doo doo doo doo doo doo
# Grandpa shark!
# Let's go hunt, doo doo doo doo doo doo
# Let's go hunt, doo doo doo doo doo doo
# Let's go hunt, doo doo doo doo doo doo
# Let's go hunt!
# Run away,…
#
#
# Good Luck!


def baby_shark_lyrics():
    c = ['Baby shark', 'Mommy shark', 'Daddy shark', 'Grandma shark', 'Grandpa shark', "Let's go hunt"]
    r = ""
    for i in c:
        r += (i + ","+" doo"*6+"\n")*3
        r += i+'!\n'

    return r+'Run away,…'
