# https://leetcode.com/problems/trapping-rain-water/description/
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

a=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# track max value in 'a'
def test_max(i):
    global m
    m = max(m, a[i])
    return m

# compute left-right max volume
m=0
max_l=[test_max(i) for i in range(0, len(a))]

# compute right-left max volume
m=0
max_r=[test_max(i) for i in range(len(a) - 1, -1, -1)]

# match direction of max_l
max_r.reverse()
# sum min intersection
s=0
for i, v in enumerate(a):
    s+=min(max_l[i], max_r[i]) - v

print(s)