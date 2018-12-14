# https://www.codewars.com/kata/55fde83eeccc08d87d0000af
#
# Write a function that returns the degree of a polynomial function:
#
# degree(x => 42);                    // 0
# degree(x => x);                     // 1
# degree(x => x * x);                 // 2
# degree(x => x * x * x);             // 3
# degree(x => 2 * x + 3 * x * x + 5); // 2
#
#     Assume that the polynomial has a maximum degree of 11
#     The input x of the polynomial function
#         must be between -11 and 11
#         use integers to get exact results without rounding errors


def degree(p):
    x = [i for i in range(12)]
    y = [[p(i) for i in x]]
    d = 0

    while True:
        if y[-1].count(y[-1][0]) == 12-d:
            return d

        y.append([y[-1][i]-y[-1][i+1] for i in range(11-d)])
        d += 1
