# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
# In a given array nums of positive integers, find three non-overlapping
# subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k
# entries.
#
# Return the result as a list of indices representing the starting position of
# each interval (0-indexed). If there are multiple answers, return the
# lexicographically smallest one.

import math

nums=[1, 2, 1, 2, 6, 7, 5, 1]
#     0  1  2  3  4  5  6  7

# subarray size
k=math.floor(len(nums)/3)

# alg:
# 1. for each adjustable window compute sums
# 2. determine max path connecting sums minimizing path cost
#
# w0    w1    w2
# [3]   [3]   [13]
# [3]   [8]   [12]
# [3]   [13]  [6]
#
# 0 -> 0 -> 0
#       `-> 1
#       `-> 2
#
# 0
#  `-> 1 -> 1
#       `-> 2

l=len(nums)

# windows
w0=[sum(nums[x:x+k]) for x in range(k*0, l-k*2-1)]
w1=[sum(nums[x:x+k]) for x in range(k*1, l-k*1-1)]
w2=[sum(nums[x:x+k]) for x in range(k*2, l-k*0-1)]

# find path
p=(0,0,0)
s=0
wl=len(w0)
for i0 in range(0, wl):
    for i1 in range(i0, wl):
        for i2 in range(i1, wl):
            s2=sum((w0[i0], w1[i1], w2[i2]))
            if s2>s:
                s=s2
                p=(i0,i1,i2)

# convert path to indices
print([i*k+v for i,v in enumerate(p)])