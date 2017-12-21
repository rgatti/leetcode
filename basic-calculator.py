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

from fractions import Fraction

class Expr:
    def __init__(self, parent=None):
        self.parent = parent
        self._op = None
        self.left = None
        self.right = None
        self.side = 'left'
    def set(self, expr):
        if self.side == 'left':
            self.left = expr
            self.side = 'right'
        elif self.side == 'right':
            self.right = expr
            self.side = None
        else:
            raise TypeError
    def op(self, op):
        # if we already have a full expression push the left side down
        if self.side == None:
            e = Expr(self)
            e.set(self.left)
            e.op(self._op)
            e.set(self.right)
            self.left = e
            self.side = 'right'
            self.right = None
        self._op = op
    def value(self):
        n0 = self.left
        n1 = self.right
        if isinstance(n0, Expr):
            n0 = n0.value()
        if isinstance(n1, Expr):
            n1 = n1.value()

        if self._op == None:
            return n0
        elif self._op == '+':
            return n0 + n1
        elif self._op == '-':
            return n0 - n1
    def __str__(self):
        n0 = self.left
        n1 = self.right
        op = self._op
        if isinstance(n0, Expr):
            n0 = '({0})'.format(n0)
        if op == None:
            op = ''
        if isinstance(n1, Expr):
            n1 = '({0})'.format(n1)
        elif n1 == None:
            n1 = ''
        return '{0} {1} {2}'.format(n0, op, n1).strip()

def push(parent):
    e = Expr(parent)
    parent.set(e)
    return e

def pop(expr):
    return expr if expr.parent == None else expr.parent

def get_root(expr):
    e = expr
    while e.parent != None:
        e = e.parent
    return e

def my_eval(expr):
    e = Expr() # root expression
    num = None
    for c in expr:
        if c == ' ':
            pass
        elif c in '0123456789': # parse number
            c = int(c)
            if num != None:
                num = (num * 10) + c
            else:
                num = c
        elif c == '(': # add subexpr
            e = push(e)
        elif c == ')': # pop subexpr
            if num != None:
                e.set(num)
                num = None
                e = pop(e)
        elif c in '+-': # add op
            if num != None:
                e.set(num)
                num = None
            e.op(c)
    # make sure final number is set
    if num != None:
        e.set(num)

    e = get_root(e)
    print('{0} = {1}'.format(e, e.value()))

#my_eval('2 + 2')
#my_eval('2 + (2 - 1)')
my_eval('(1+(4+5+2)-3)+(6+8)')
