#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        point = 0 
        max_length = 0
        chars = set()
        charslist = list()
        for i in range(len(s)):
            if s[i] in chars:
                while s[point] != s[i]:
                    chars.remove(s[point])
                    point += 1
                point += 1
            else:
                chars.add(s[i])
                max_length = max(max_length, i - point + 1)
# @lc code=end

