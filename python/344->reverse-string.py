# LeetCode 344 - Reverse String
# Difficulty: Easy
# Status: Accepted
# Topic: Array, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def reverseString(self, s):
        s[:] = s[::-1]
