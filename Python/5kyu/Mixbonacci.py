# https://www.codewars.com/kata/5811aef3acdf4dab5e000251
#
# This is the first of my "-nacci" series. If you like this
# kata, check out the zozonacci sequence too.
# Task
#
#     Mix -nacci sequences using a given pattern p.
#     Return the first n elements of the mixed sequence.
#
# Rules
#
#     The pattern p is given as a list of strings (or array
#     of symbols in Ruby) using the pattern mapping below
#     (e. g. ['fib', 'pad', 'pel'] means take the next fibonacci,
#     then the next padovan, then the next pell number and so on).
#     When n is 0 or p is empty return an empty list.
#     If the length of p is more than n repeat the pattern.
#
# Examples
#
#             0  1  2  3  4
# ----------+------------------
# fibonacci:| 0, 1, 1, 2, 3 ...
# padovan:  | 1, 0, 0, 1, 0 ...
# pell:     | 0, 1, 2, 5, 12 ...
#
# pattern = ['fib', 'pad', 'pel']
# n = 6
# #          ['fib',        'pad',      'pel',   'fib',        'pad',      'pel']
# # result = [fibonacci(0), padovan(0), pell(0), fibonacci(1), padovan(1), pell(1)]
# result = [0, 1, 0, 1, 0, 1]
#
# pattern = ['fib', 'fib', 'pel']
# n = 6
# #          ['fib', 'fib', 'pel', 'fib', 'fib', 'pel']
# # result = [fibonacci(0), fibonacci(1), pell(0), fibonacci(2), fibonacci(3), pell(1)]
# result = [0, 1, 0, 1, 2, 1]
#
# Sequences
#
#     fibonacci : 0, 1, 1, 2, 3 ...
#     padovan: 1, 0, 0, 1, 0 ...
#     jacobsthal: 0, 1, 1, 3, 5 ...
#     pell: 0, 1, 2, 5, 12 ...
#     tribonacci: 0, 0, 1, 1, 2 ...
#     tetranacci: 0, 0, 0, 1, 1 ...
#
# Pattern mapping
#
#     'fib' -> fibonacci
#     'pad' -> padovan
#     'jac' -> jacobstahl
#     'pel' -> pell
#     'tri' -> tribonacci
#     'tet' -> tetranacci
#
# If you like this kata, check out the zozonacci sequence.


def mixbonacci(pattern, length):
    if pattern == [] or length == 0:
        return []
    else:
        result = []
        fib_a, fib_b = 0, 1
        pad_a, pad_b, pad_c = 1, 0, 0
        pel_a, pel_b = 0, 1
        jac_a, jac_b = 0, 1
        tri_a, tri_b, tri_c = 0, 0, 1
        tet_a, tet_b, tet_c, tet_d = 0, 0, 0, 1
        for i in range(length):
            if pattern[i % len(pattern)] == 'fib':
                result.append(fib_a)
                fib_a, fib_b = fib_b, fib_a + fib_b

            elif pattern[i % len(pattern)] == 'pad':
                    result.append(pad_a)
                    pad_a, pad_b, pad_c = pad_b, pad_c, pad_b + pad_a

            elif pattern[i % len(pattern)] == 'pel':
                    result.append(pel_a)
                    pel_a, pel_b = pel_b, 2*pel_b + pel_a

            elif pattern[i % len(pattern)] == 'jac':
                    result.append(jac_a)
                    jac_a, jac_b = jac_b, jac_b + 2*jac_a

            elif pattern[i % len(pattern)] == 'tri':
                    result.append(tri_a)
                    tri_a, tri_b, tri_c = tri_b, tri_c, tri_c + tri_b + tri_a

            elif pattern[i % len(pattern)] == 'tet':
                    result.append(tet_a)
                    tet_a, tet_b, tet_c, tet_d = tet_b, tet_c, tet_d, tet_d + tet_c + tet_b + tet_a

        return result
