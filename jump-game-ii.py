# https://leetcode.com/problems/jump-game-ii/
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# For example:
#     Given array A = [2,3,1,1,4]
#     The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#     Note:
#         You can assume that you can always reach the last index.
#

def jump(nums):
    i = 0
    jumps = 0
    while True:
        jumps += 1
        window = nums[i]
        # if our current window can jump us to the end of the list
        # we're done
        if i + 1 + window >= len(nums):
            break
        choices = nums[i + 1: i + 1 + window]
        weights = [pos - (window - val) \
                for val, pos in enumerate(choices)]
        best = weights.index(max(weights))
        #print("index: {0}\nchoices: {1}\nweights: {2}\nbest: {3}".format(i, choices, weights, best))
        i = i + 1 + best
    print(jumps)

jump([2,3,1,1,4])
jump([1,1,1,1,4])
jump([4,3,1,1,4])
jump([2,5,1,1,1])
jump([4,3,1,1,4])
jump([4,5,1,1,1])
