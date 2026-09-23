# LeetCode 1 - Two Sum
# Difficulty: Easy
# Status: Accepted
# Topic: Array, Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):

    def twoSum(self, nums, target):

        seen = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
