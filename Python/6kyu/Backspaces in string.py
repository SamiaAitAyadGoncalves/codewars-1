# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3
#
# Assume `"#"` is like a backspace in string. This means that string `"a#bc#d"`
# actually is `"bd"`
#
# Your task is to process a string with `"#"` symbols.
#
#
# ## Examples
#
#
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""


def clean_string(s):
    result = ''
    for letter in s:
        if letter != '#':
            result += letter
        else:
            result = result[:-1]
    return result
