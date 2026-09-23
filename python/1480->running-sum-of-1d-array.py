# LeetCode 1480 - Running Sum of 1d Array
# Difficulty: Easy
# Status: Accepted
# Topic: Array, Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
