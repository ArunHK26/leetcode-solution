# LeetCode 58 - Length of Last Word
# Difficulty: Easy
# Status: Accepted
# Topic: String
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):

    def lengthOfLastWord(self, s):

        words = s.split()

        return len(words[-1])
