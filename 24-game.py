# You have 4 cards each containing a number from 1 to 9. You need to judge
# whether they could operated through *, /, +, -, (, ) to get the value of 24.
#
# Example 1
#######
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
#
# Example 2
#######
# Input: [1, 2, 1, 2]
# Output: False

from fractions import Fraction
import math

# Represents a single mathematical operation between two items. These items
# can be integers or Op instances.
class Op:
    def __init__(self, in0, in1, op):
        self.in0 = in0
        self.in1 = in1
        self.op = op
        # get value if inputs are Op instances
        self.in0v = _op_get_value(in0)
        self.in1v = _op_get_value(in1)
        # make sure fractions are rational, for +, -, * just eval()
        if self.op == '/':
            if self.in1v == 0:
                self.val = float('nan')
            else:
                self.val = Fraction(self.in0v, self.in1v)
        else:
            self.val = eval('({0} {1} {2})'.format(self.in0, self.op, self.in1))
    def value(self):
        return self.val
    def __str__(self):
            return '({0} {1} {2})'.format(self.in0, self.op, self.in1)
    def __lt__(self, other):
        return self.val < _op_get_value(other)
    def __le__(self, other):
        return self.val <= _op_get_value(other)
    def __gt__(self, other):
        return self.val > _op_get_value(other)
    def __ge__(self, other):
        return self.val >= _op_get_value(other)
    def __eq__(self, other):
        return self.val == _op_get_value(other)
    def __ne__(self, other):
        return self.val != _op_get_value(other)

# Constructor returns a list of all mathematical operations for two items.
def op(in0, in1):
    return [ Op(in0, in1, o) for o in '+-*/' ]

# Utility function to return the value given an object. This might be an
# integer or an Op instance.
def _op_get_value(obj):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, Op):
        return obj.value()
    else:
        raise TypeError

# Bascially, this function generates levels 2 and 3 of a computational forest
# and checks if the number 24 exists.
def _test_24(num0, num1, num2, num3):
    # generate lists of all mathematical operations
    v0 = op(num0, num1)
    v1 = op(num2, num3)

    # for each pair of results generate a new list of ops
    for i in v0:
        for j in v1:
            fin = op(i, j)
            # search this final list for 24
            for f in fin:
                if f == 24:
                    return True, f
    return False, None

# Starting function
def judge_point_24(nums):
    print('Can {0} = 24?'.format(nums), end=' ')
    # check each ordering of inputs
    for t in [(0,1,2,3), (0,2,1,3), (0,3,1,2)]:
        success, exp = _test_24(nums[t[0]], nums[t[1]], nums[t[2]], nums[t[3]])
        if success:
            print('Yes: {0}'.format(exp))
            return
    print('No')


# Test all enumerations of nums 1-9
for nums in [(i,j,k,l)
        for i in range(1,10)
        for j in range(1,10)
        for k in range(1,10)
        for l in range(1,10)]:
    judge_point_24(nums)
