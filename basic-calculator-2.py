# https://leetcode.com/problems/basic-calculator
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the
# plus + or minus sign -, non-negative integers and empty spaces .
#
# You may assume that the given expression is always valid.
#
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23

def shift_add(num, c):
    a = num if num != None else 0
    b = int(c)
    return a * 10 + b

def compute(l, r, op):
    if op == '+':
        return l + r
    elif op == '-':
        return l - r
    else:
        return r

def my_eval(expr):
    sub = []  # subexpressions
    left = right = op = None
    for c in expr:
        if c == ' ': # ignore spaces
            pass
        elif c in '0123456789': # parse number
            right = shift_add(right, c)
        elif c in '+-':
            left = compute(left, right, op)
            right = None
            op = c
        elif c == '(':
            sub.append((left,op))
            left = op = None
        elif c == ')':
            left = compute(left, right, op)
            right = left
            left, op = sub.pop()
    left = compute(left, right, op)
    print('"{0}" = {1}'.format(expr, left))

# Tests
##############
my_eval('')
my_eval('2 + 2')
my_eval('2 + 2 - 1')
my_eval('2 + (2 - 1)')
my_eval('(1+(4+5+2)-3)+(6+8)')
my_eval('(2) + 2')
