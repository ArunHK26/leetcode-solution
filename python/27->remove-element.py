# LeetCode 27 - Remove Element
# Difficulty: Easy
# Status: Accepted
# Topic: Array, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
