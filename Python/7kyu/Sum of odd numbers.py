# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
#
# Given the triangle of consecutive odd numbers:
#
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
#
#
# Calculate the row sums of this triangle from the row index
# (starting at index 1) e.g.:
#
# javascript
# rowSumOddNumbers(1); // 1
# rowSumOddNumbers(2); // 3 + 5 = 8
#
# ruby
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8
#
# rust
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8
#
# python
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8
#
#
# java
# rowSumOddNumbers(1); // 1
# rowSumOddNumbers(2); // 3 + 5 = 8
#
#
# csharp
# rowSumOddNumbers(1); // 1
# rowSumOddNumbers(2); // 3 + 5 = 8
#
#
# fsharp
# rowSumOddNumbers 1 // 1
# rowSumOddNumbers 2 // 3 + 5 = 8
#
#
# haskell
# rowSumOddNumbers 1 -- 1
# rowSumOddNumbers 2 -- 3 + 5 = 8
#
# r
# row_sum_odd_numbers(1) # 1
# [1] 1
# row_sum_odd_numbers(2) # 3 + 5
# [1] 8
#
# if:nasm
# row_sum_odd_numbers:
#
# nasm
# mov rdi 1
# call row_sum_odd_numbers    ; rax <- 1
#
# mov rdi 2
# call row_sum_odd_numbers   ; rax <- 3 + 5


def row_sum_odd_numbers(n):
    start = sum([(i)*2 for i in range(0,n)]) + 1
    return sum([i*2 for i in range(n)])+start*n
