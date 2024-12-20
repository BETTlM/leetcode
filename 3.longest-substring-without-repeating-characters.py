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
        max_len = 0
        start = 0
        used = []
        for i in range(len(s)):
            if s[i] in used:
                start = max(start, used.index(s[i]) + 1)
            used.append(s[i])
            max_len = max(max_len, i - start + 1)
        return max_len
    
# @lc code=end

