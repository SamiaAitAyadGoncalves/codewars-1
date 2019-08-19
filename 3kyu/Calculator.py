# https://www.codewars.com/kata/5235c913397cbf2508000048
#
# Create a simple calculator that given a string of operators (+ - * and /) and
# numbers separated by spaces returns the value of that expression
#
# Example:
#
# python
# Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
#
# ruby
# Calculator.new.evaluate("2 / 2 + 3 * 4 - 6") # => 7
#
# java
# Calculator.evaluate("2 / 2 + 3 * 4 - 6") // => 7
#
# haskell
# Calculator.evaluate "2 / 2 + 3 * 4 - 6" // => 7.0
#
#
# Remember about the order of operations! Multiplications and divisions have a
# higher priority and should be performed left-to-right. Additions and subtractions
# have a lower priority and should also be performed left-to-right.


class Calculator(object):
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b

    def evaluate(self, s):
        d= {'/': self.div, '*': self.mul, '+': self.add, '-': self.sub}
        s = s.split(' ')

        while '/' in s  or '*' in s:
            for i in range(len(s)):
                if s[i] == '/' or s[i] == '*':
                    temp = d[s[i]](float(s[i-1]), float(s[i+1]))
                    s.pop(i+1)
                    s.pop(i)
                    s.pop(i-1)
                    s.insert(i-1, str(temp))
                    break

        while '+' in s  or '-' in s:
            for i in range(len(s)):
                if s[i] == '+' or s[i] == '-':
                    temp = d[s[i]](float(s[i-1]), float(s[i+1]))
                    s.pop(i+1)
                    s.pop(i)
                    s.pop(i-1)
                    s.insert(i-1, str(temp))
                    break

        return float(s[0])
