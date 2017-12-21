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


# A basic expression tree:
# - evaluate a left/right expression +/-
# - push down a subexpression for 1+1+1 scenarios
# - print the expression including subexpressions
class Expr:
    def __init__(self, parent=None):
        self.parent = parent
        self._set_defaults()
    def _set_defaults(self):
        self.left = self.right = self._op = None
        self.side = 'left'
    def set(self, expr):
        """ Set a value for the current side (left/right). """
        if self.side == 'left':
            self.left = expr
        elif self.side == 'right':
            self.right = expr
        else:
            raise TypeError
        self.side = 'right' if self.side == 'left' else None
    def op(self, op):
        """ Set the operation for this expression. """
        # if we already have an expression push the left side down
        if self.side == None:
            n0, n1, _op = self.left, self.right, self._op
            self._set_defaults()
            e = push(self)
            e.set(n0)
            e.op(_op)
            e.set(n1)
        self._op = op
    def value(self):
        """ Evaluate this expression and all subexpressions. """
        n0, n1 = self.left, self.right
        # eval subexpressions
        if isinstance(n0, Expr):
            n0 = n0.value()
        if isinstance(n1, Expr):
            n1 = n1.value()
        # compute
        if self._op == None:
            return n0
        elif self._op == '+':
            return n0 + n1
        elif self._op == '-':
            return n0 - n1
    def __str__(self):
        n0, n1, op = self.left, self.right, self._op
        # subexpr formatting
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
    """ Push a new expression onto the tree. """
    e = Expr(parent)
    parent.set(e)
    return e

def pop(expr):
    """ Return the immediate parent or self it's the root. """
    return expr if expr.parent == None else expr.parent

def get_root(expr):
    """ Walk up the full expression tree. """
    e = expr
    while e.parent != None:
        e = e.parent
    return e

def my_eval(expr):
    e = Expr() # root expression
    num = None
    for c in expr:
        if c == ' ': # ignore spaces
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
        elif c in '+-': # set operator
            if num != None:
                e.set(num)
                num = None
            e.op(c)
    # make sure any final number is set
    if num != None:
        e.set(num)
    # find expression root & evaluate
    e = get_root(e)
    print('{0} = {1}'.format(e, e.value()))


# Tests
##############
my_eval('2 + 2')
my_eval('2 + (2 - 1)')
my_eval('(1+(4+5+2)-3)+(6+8)')
