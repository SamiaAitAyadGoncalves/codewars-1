# https://www.codewars.com/kata/59d727d40e8c9dd2dd00009f
#
# You are given a (small) check book as a - sometimes - cluttered
# (by non-alphanumeric characters) string:
#
# "1000.00
# 125 Market 125.45
# 126 Hardware 34.95
# 127 Video 7.45
# 128 Book 14.32
# 129 Gasoline 16.10"
#
# The first line shows the original balance. Each other line (when not blank)
# gives information: check number, category, check amount.
#
# First you have to clean the lines keeping only letters, digits, dots and spaces.
#
# Then return a report as a string (underscores show spaces -- don't put them
# in your solution. They are there so you can see them and how many of them you need):
#
# "Original_Balance:_1000.00
# 125_Market_125.45_Balance_874.55
# 126_Hardware_34.95_Balance_839.60
# 127_Video_7.45_Balance_832.15
# 128_Book_14.32_Balance_817.83
# 129_Gasoline_16.10_Balance_801.73
# Total_expense__198.27
# Average_expense__39.65"
#
# On each line of the report you have to add the new balance and then in the
# last two lines the total expense and the average expense. So as not to have a too long result string we don't ask for a properly formatted result.
# Notes
#
#     One (or more) line can be blank.
#     Round to 2 decimals your results.
#     The line separator of results may depend on the language
#     \n or \r\n. You can see examples in the "Sample tests".


import re

def clean(s):
    return re.sub('[^0-9a-zA-Z. \n]', '', s)

def own_round(n):
    result = str(round(n, 2))
    if result[-2] == '.':
        result += '0'

    return result

def balance(book):
    book_clean = clean(book).split('\n')
    originalb = book_clean[0]

    result = ['Original Balance: ' + own_round(float(originalb))]

    current_balance = float(originalb)

    count = 0
    for row in book_clean[1:]:
        if row != '':
            count += 1
            arr = row.split(' ')
            current_balance -= float(arr[2])
            result.append(arr[0] + ' ' + arr[1] + ' ' + own_round(float(arr[2])) + ' Balance ' + own_round(current_balance))

    avg = (float(originalb) - current_balance)/count
    result.append('Total expense  ' + own_round(float(originalb) - current_balance))
    result.append('Average expense  ' + own_round(avg))

    return '\r\n'.join(result)
