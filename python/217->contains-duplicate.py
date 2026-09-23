# LeetCode 217 - Contains Duplicate
# Difficulty: Easy
# Status: Accepted
# Topic: Array, Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        
        return len(nums) != len(set(nums))
